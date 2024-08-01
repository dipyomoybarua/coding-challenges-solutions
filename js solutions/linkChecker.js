const axios = require('axios');
const cheerio = require('cheerio');
const url = require('url');

async function findBrokenLinks(baseUrl) {
  const queue = [baseUrl];
  const visited = new Set();
  const brokenLinks = [];
  const maxConcurrency = 10; // Maximum number of concurrent requests
  let concurrentRequests = 0;

  async function processUrl(currentUrl) {
    try {
      const response = await axios.get(currentUrl, { timeout: 5000 }); // Set timeout to 5 seconds

      if (response.status !== 200) {
        console.log(`Broken Link: ${currentUrl} (status: ${response.status})`);
        brokenLinks.push({ url: currentUrl, status: response.status });
      }

      const $ = cheerio.load(response.data);
      const links = $('a');

      links.each((index, element) => {
        let link = $(element).attr('href');

        if (link) {
          link = url.resolve(baseUrl, link);

          if (link.startsWith(baseUrl) && !visited.has(link)) {
            queue.push(link);
          }
        }
      });
    } catch (error) {
      if (error.response) {
        console.log(`Broken Link: ${currentUrl} (status: ${error.response.status})`);
        brokenLinks.push({ url: currentUrl, status: error.response.status });
      } else {
        console.error(`Error processing ${currentUrl}: ${error.message}`);
      }
    } finally {
      visited.add(currentUrl);
      concurrentRequests--;
      processQueue();
    }
  }

  async function processQueue() {
    while (concurrentRequests < maxConcurrency && queue.length > 0) {
      const currentUrl = queue.shift();
      if (!visited.has(currentUrl)) {
        concurrentRequests++;
        await processUrl(currentUrl);
      }
    }
  }

  await processQueue(); // Start processing the initial queue

  console.log('Finished checking links.');
  return brokenLinks;
}

// Example usage:
findBrokenLinks('https://www.cricbuzz.com/').then((brokenLinks) => {
  console.log('Broken links found:', brokenLinks);
});
