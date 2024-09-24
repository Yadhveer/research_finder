import requests

def search_faculty(faculty_list, keyword_list, serpapi_api_key):
    faculty_with_keywords = []
    
    for faculty in faculty_list:
        # Step 1: Search faculty on Google Scholar using SerpAPI
        params = {
            "engine": "google_scholar",
            "q": faculty,
            "api_key": serpapi_api_key
        }

        response = requests.get("https://serpapi.com/search.json", params=params)
        data = response.json()

        # Step 2: Check if results contain publications with the keywords
        found_keywords = False
        for result in data.get("organic_results", []):
            title = result.get("title", "").lower()
            snippet = result.get("snippet", "").lower()

            for keyword in keyword_list:
                if keyword.lower() in title or keyword.lower() in snippet:
                    found_keywords = True
                    break

        # Step 3: If found, add faculty to the list
        if found_keywords:
            faculty_with_keywords.append(faculty)

    return faculty_with_keywords


faculty_names = ["PUT IN THE LIST OF FACULTY YOU WANT TO SEARCH FROM HERE"]                                #Eg: [John Doe, Jane Smith, Tony]
keywords = ["TYPE IN KEYWORDS THAT YOU WANT YOUR FACULTY MEMBERS TO HAVE RESEARCH PAPERS IN"]              #Eg: [Cybersecurity, Privacy, Forensics]
serpapi_api_key = "YOUR_SECRET_API_KEY"  # Get your key from SerpAPI

result = search_faculty(faculty_names, keywords, serpapi_api_key)

print("Faculty with relevant research:")
for faculty in result:
    print(faculty)
