const { Builder, By, until } = require('selenium-webdriver');
const assert = require('assert');

async function verifyCompanyPercentageChange(expectedData) {
  let driver;

  try {
    // Initialize WebDriver
    driver = await new Builder().forBrowser('chrome').build();

    // Navigate to the URL
    await driver.get('https://demo.guru99.com/test/web-table-element.php');

    // Wait for the table to load
    let table = await driver.wait(until.elementLocated(By.xpath("//table[@class='dataTable']")), 10000);

    // Find all rows in the table
    let rows = await table.findElements(By.xpath(".//tr"));

    // Iterate through each row (skip the first row as it contains headers)
    for (let row of rows.slice(1)) {
      try {
        // Extract company name and % change from the row
        let cells = await row.findElements(By.xpath(".//td"));
        let companyName = await cells[0].getText();
        let actualChange = await cells[4].getText();

        // Verify against expected data if it exists
        if (expectedData.hasOwnProperty(companyName)) {
          let expectedPattern = expectedData[companyName]; // Expected pattern for % change
          let regex = new RegExp(`^\\+?\\s?\\d+\\.?\\d*$`); // Corrected regex pattern
          
          assert.ok(regex.test(actualChange.trim()), `Expected pattern ${expectedPattern} for ${companyName} but found ${actualChange.trim()}`);
          console.log(`Test passed for ${companyName}`);
        } else {
          console.warn(`No expected data found for ${companyName}. Skipping verification.`);
        }

      } catch (error) {
        console.error(`Test failed for row ${row}: ${error.message}`);
        throw error;
      }
    }

    console.log('All tests passed');

  } finally {
    // Quit the driver
    if (driver) {
      await driver.quit();
    }
  }
}

const dynamicExpectedData = {
  'NCC': '+',
  'CESC Ltd.': '+',
  'IRB Infrastructure': '+',
  
};

// Run the test with dynamic expected data
verifyCompanyPercentageChange(dynamicExpectedData).catch(err => {
  console.error('Test failed', err);
});
