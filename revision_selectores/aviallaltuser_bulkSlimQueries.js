const aviallaltuserCtrl = {};

const puppeteer = require("puppeteer-extra");
const StealthPlugin = require("puppeteer-extra-plugin-stealth");
const InitialBrowser = require("../../../utils/initialValues/browser");
const { sleepTime, shortTime, longTime, randomDelay } = require("../../../utils/initialValues/constants");
const InitialPage = require("../../../utils/initialValues/page");
const login = require("../helpers/login");
const { explorerSaveData } = require("../../../utils/axios/saveData");
const { emailNotificationSender } = require("../../../utils/queue/emailNotificationSender");
const partList = require(`../helpers/searchQueries.json`);

puppeteer.use(StealthPlugin());

const vendor = 'aviallaltuser';
const BASE_URL = "https://shop.boeing.com/aviation-supply/";
const LOGIN_URL = "https://shop.boeing.com/aviation-supply/login";
let page;
let browser;

aviallaltuserCtrl.bulkSlimQueries_aviallaltuser = async (req, res) => {
    let today = Date.now();
    console.log("----LOG: Init scrapper " + today);

    try {
        // insert 

        browser = await InitialBrowser(puppeteer);
        page = await InitialPage(browser, LOGIN_URL);

        await page.waitForTimeout(sleepTime)

        const { needsLogin, userRef, dataCutter, pages, message } = req.body;
        if (needsLogin === 'yes') {
            const signin = await login(page, userRef);
            if (signin) {
                await page.waitForTimeout(sleepTime);
            } else {
                throw new Error("Error Login");
            }
        }

        const testURL = null // '1776-1'
        const testPart = null // [] // [partList[0]]
        // for (let i = 0; i < 5; i++) {
        //     const random = Math.floor(Math.random() * partList.length)
        //     console.log(random)
        //     testPart.push(partList[random])
        // }

        let categoryCounter = dataCutter
        const partListSession = partList.slice(categoryCounter)
        console.log(partListSession.length)
        for (const partURL of testPart ? testPart : partListSession) {
            let subCatPartPage = pages; // zero(0) based page system
            let nextPage = true

            const actualUrl = await page.url()
            if (actualUrl != BASE_URL + `search?q=${testURL ? testURL : partURL.partNumber}%3Arelevance&text=${testURL ? testURL : partURL.partNumber}&isCallPandA=false&showPage=20&page=${subCatPartPage}`) {
                await page.goto(BASE_URL + `search?q=${testURL ? testURL : partURL.partNumber}%3Arelevance&text=${testURL ? testURL : partURL.partNumber}&isCallPandA=false&showPage=20&page=${subCatPartPage}`, {
                    timeout: 0
                })
            }
            await page.waitForTimeout(shortTime)

            if (await page.$('div#brands.adobeNoResults')) {
                console.log(`${categoryCounter++} - Sorry, we can't find any results`)
                await page.waitForTimeout(shortTime)
                continue
            }

            // while (nextPage) {
            await page.waitForSelector('#resultsList div.productLineItem div.details > a', {
                timeout: 45000
            })
            await page.waitForTimeout(15000)//10000
            const subCatPartsArray = await page.$$('#resultsList div.productLineItem')
            for (const partElement of subCatPartsArray) {
                // if (!(await partElement.$('#prodNetPrice'))) {
                //     console.log(`${categoryCounter} - Request Quote! - ${subCatPartPage}`)
                //     await page.waitForTimeout(2000)
                //     continue
                // }
                const subCatPart = {
                    partNumberUnpunctuated: await partElement.$eval('div.details > a', element => element.innerText),
                    description: await partElement.$eval('div.details > div.basefont.breakWord.level5', element => element.innerText),
                    category: 'Aircraft Parts', // partURL.subCategoryName,
                    subCategory: partURL.categoryName,
                    nsn: '',
                    niin: '',
                    pma: '',
                    alternativePartNumber: [],
                    manufacturer: [{ name: await partElement.$eval('div.product-item-details a.basefont.level5.light.notranslate', element => element.innerText) }],
                    location: [{
                        warehouse: 'Aviall',
                        stock: await partElement.$('div.totalInventoryCount')
                            ? parseInt(await partElement.$eval('div.totalInventoryCount', element => element.innerText.replace(',', '')))
                            : 0
                    }],
                    imgUrl: await partElement.$eval('div.product-item-details img', element => element.getAttribute('id')) !== ''
                        ? await partElement.$eval('div.product-item-details img', element => element.getAttribute('src'))
                        : null,
                    weight: 0,
                    vendor: 'aviallaltuser',
                    quotes: [{
                        price: await partElement.$('#prodNetPrice')
                            ? parseFloat(await partElement.$eval('#prodNetPrice', element => element.innerText.replace(/[$,]+/g, "")))
                            : null,
                        createdAt: Date.now()
                    }],
                    unitMeasure: '',
                    condition: '',
                    minqty: '',
                    url: await partElement.$eval('div.details > a', element => 'https://shop.boeing.com' + element.getAttribute('href')),
                    downloadfile: message
                        ? message
                        : ''
                }

                // console.log(subCatPart)
                const saveData = await explorerSaveData(subCatPart);
                if (saveData.data && saveData.data.status !== 200) {
                    console.log("---LOG_ERROR: ", saveData.data.err);
                    throw new Error(`Error: ${saveData.data.err}`);
                } else {
                    console.log("---LOG_SUCCESS: ", `${categoryCounter} - ${saveData.data.partnumber} - ${subCatPartPage}`);
                }
                await page.waitForTimeout(2000)
            }
            await page.waitForTimeout(randomDelay('3'))

            //     if (await page.$('#pageSelePagination > ul > li.nextNum > a')) {
            //         ++subCatPartPage
            //         await page.click('#pageSelePagination > ul > li.nextNum > a');
            //     } else {
            //         nextPage = false;
            //         if (pages > 1) {
            //             throw new Error('Reset the dataCutter and page parameter!')
            //         }
            //     }
            // }
            ++categoryCounter
        }

        await page.close();
        await browser.close();

        // await new Promise(function (resolve) {
        //     const random = Math.floor(Math.random() * timeBetweenSessions) + 60000
        //     console.log(`Waiting ${Math.round((random / 1000) / 60)}min`);
        //     setTimeout(resolve, random);
        // });

        // inster here

        return res
            .json({
                status: 200,
                message: "Successfully searched",
            })
    } catch (error) {
        const errorURL = await page.url();
        await page.close();
        await browser.close();
        console.log({
            status: 500,
            message: `Error: 500 > Running Scrapper | inURL:${errorURL}`,
            logs: error.message
        });
        return res.json({
            status: 500,
            message: `Error: 500 > Running Scrapper | inURL:${errorURL}`,
            logs: error.message
        });
    };
}

module.exports = aviallaltuserCtrl;
