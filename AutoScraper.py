from flask import Flask, jsonify
from autoscraper import AutoScraper

app = Flask(__name__)

@app.route("/")
def scrape_events():
    # URL of the website to scrape
    url = "https://allsportdb.com/"
    
    # Look for title, sport, competition, country, locale, date
    wanted_list = ['Formula 1 - Australian Grand Prix', 'Motor Sports', 'Formula 1', 'Australia', 'Melbourne']
    
    # Build a scraping model
    scraper = AutoScraper()
    result = scraper.build(url, wanted_list)

    # Train model with similar results
    result = scraper.get_result_similar("https://allsportdb.com/?week=1", grouped=True)
    
    return jsonify(result)
    # Set aliases and save ruleset
    #scraper.set_rule_aliases({'rule_2eid': 'Date', 'rule_30oz': })
    
    # Render a template with the extracted data


if __name__ == "__main__":
    app.run(debug=True)