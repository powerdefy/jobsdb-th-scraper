from python_graphql_client import GraphqlClient

endpoint = (
    "https://xapi.supercharge-srp.co/job-search/graphql?country=th&isSmartSearch=true"
)

query = """
query getLegacyJobs($country: String, $locale: String, $keyword: String, $createdAt: String, $jobFunctions: [Int], $categories: [String], $locations: [Int], $careerLevels: [Int], $minSalary: Int, $maxSalary: Int, $salaryType: Int, $candidateSalary: Int, $candidateSalaryCurrency: String, $datePosted: Int, $jobTypes: [Int], $workTypes: [String], $industries: [Int], $page: Int, $pageSize: Int, $companyId: String, $userAgent: String, $accNums: Int, $subAccount: Int, $minEdu: Int, $maxEdu: Int, $edus: [Int], $minExp: Int, $maxExp: Int, $seo: String, $searchFields: String, $candidateId: ID, $isDesktop: Boolean, $isCompanySearch: Boolean, $sort: String, $sVi: String, $duplicates: String, $flight: String, $solVisitorId: String) {
  jobs(country: $country, locale: $locale, keyword: $keyword, createdAt: $createdAt, jobFunctions: $jobFunctions, categories: $categories, locations: $locations, careerLevels: $careerLevels, minSalary: $minSalary, maxSalary: $maxSalary, salaryType: $salaryType, candidateSalary: $candidateSalary, candidateSalaryCurrency: $candidateSalaryCurrency, datePosted: $datePosted, jobTypes: $jobTypes, workTypes: $workTypes, industries: $industries, page: $page, pageSize: $pageSize, companyId: $companyId, userAgent: $userAgent, accNums: $accNums, subAccount: $subAccount, minEdu: $minEdu, edus: $edus, maxEdu: $maxEdu, minExp: $minExp, maxExp: $maxExp, seo: $seo, searchFields: $searchFields, candidateId: $candidateId, isDesktop: $isDesktop, isCompanySearch: $isCompanySearch, sort: $sort, sVi: $sVi, duplicates: $duplicates, flight: $flight, solVisitorId: $solVisitorId) {
    ...LegacyCompat_SearchResult
  }
}
fragment LegacyCompat_SearchResult on SearchResult {
  total
}
"""

variables = {
    "keyword": "",
    "jobFunctions": [],
    "locations": [],
    "salaryType": 1,
    "jobTypes": [],
    "createdAt": None,
    "careerLevels": [],
    "page": 1,
    "country": "th",
    "categories": [],
    "workTypes": [],
    "userAgent": "Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2011_0_1)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/87.0.4280.88%20Safari/537.36",
    "industries": [],
    "locale": "en",
}

client = GraphqlClient(endpoint=endpoint)


async def jobs_db_scrap(keyword) -> dict:
    variables["keyword"] = keyword
    data = await client.execute_async(query=query, variables=variables)
    return data
