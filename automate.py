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

# Example usage:
faculty_names = ["GEETHA MARY A", "SENTHIL KUMAR K", "PRAKASH G", "SIVA SHANMUGAM G","MURUGAN K", "MADIAJAGAN M", "AJU D", "DILIPKUMAR S","THAMIZHARASAN S", 
    "NITHYA N S", 
    "SAIRABANU J", 
    "KUMARESAN A", 
    "PRAKASH G", 
    "SATISH C.J", 
    "TAMIZHSELVI SP", 
    "RAMANI S", 
    "DILIPKUMAR S", 
    "ANURADHA D", 
    "VIMALA DEVI K", 
    "BASKARAN P", 
    "SIVAPRAKASH S", 
    "MURUGAN K", 
    "JAYAKUMAR K", 
    "MARY MEKALA A", 
    "MANIKANDAN K", 
    "JEEVANAJYOTHI PUJARI", 
    "NAGA RAJA G", 
    "PAVITHRA M", 
    "SUNIL KUMAR", 
    "ROHINI S", 
    "THANGARAMYA K", 
    "S M FAROOQ", 
    "UMAMAHESWARI M", 
    "MURUGAN K", 
    "BALAJI N", 
    "SIVA SANKARI S", 
    "MANIKANDAN G", 
    "MARY MEKALA A", 
    "SREETHAR S", 
    "PRAKASH G", 
    "JENICKA S", 
    "RAMANI S", 
    "KATARI BALAKRISHNA", 
    "SWETHA N G", 
    "NIVITHA K", 
    "ILAYARAJA V", 
    "THAMIZHARASAN S", 
    "MARIAPPAN R", 
    "LATHA REDDY N", 
    "KOVENDAN A.K.P", 
    "DEEPIKAA S", 
    "NIVETHITHA K",
    "ARUNKUMAR A",
    "DINESH R",
    "PRIYA V",
    "RAMYA.G",
    "CHARANYA R",
    "SARITHA MURALI",
    "MOHANA PRIYA P",
    "SOMASUNDARAM S K",
    "CHANDRA MOHAN B",
    "PARTHASARATHY G"]  # Replace with your list of faculty names
keywords = ["cybersecurity", "fuzzing", "pentesting", "malware", "data privacy", "cryptography", "network security" ]  # Your keywords
serpapi_api_key = "63768389163be52acda96725543d607a3ee2b0fdbf5f4956a1407dd28df38626"  # Get your key from SerpAPI

result = search_faculty(faculty_names, keywords, serpapi_api_key)

print("Faculty with relevant research:")
for faculty in result:
    print(faculty)
