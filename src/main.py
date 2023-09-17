import requests
import json

from concurrent.futures import ProcessPoolExecutor

jsonData = {
    'operationName': 'cosmo_VideoCategory',
    'variables': {
        'categoryCode': 'MNU0000141',
        'page': 1,
        'filterSaleType': 'MIHOUDAI',
        'sortOrder': 'POPULAR',
    },
    'query': 'query cosmo_VideoCategory($categoryCode: ID!, $page: Int!, $sortOrder: PortalSortOrder!, $dubSubFilter: DubSubType, $filterSaleType: SaleType) {\n  webfront_searchVideo(\n    categoryCode: $categoryCode\n    page: $page\n    pageSize: 30\n    sortOrder: $sortOrder\n    dubSubFilter: $dubSubFilter\n    filterSaleType: $filterSaleType\n  ) {\n    pageInfo {\n      page\n      pageSize\n      pages\n      results\n      __typename\n    }\n    titles {\n      ...TitleCard\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TitleCard on Title {\n  id\n  titleName\n  isNew\n  catchphrase\n  rate\n  titleComment\n  titleHeading\n  productionYear\n  updateOfWeek\n  lastEpisode\n  nfreeBadge\n  hasSubtitle\n  hasDub\n  paymentBadgeList {\n    code\n    __typename\n  }\n  productLineupCodeList\n  thumbnail {\n    standard\n    __typename\n  }\n  exclusiveBadgeCode\n  __typename\n}\n',
}

def getTitlesByPage(page):
  jsonData['variables']['page'] = page
  response = requests.post('https://cc.unext.jp/', json=jsonData).json()
  # print(response)
  return response['data']['webfront_searchVideo']['titles']

def getTitlesByCategoryCode(categoryCode):
  jsonData['variables']['categoryCode'] = categoryCode
  response = requests.post('https://cc.unext.jp/', json=jsonData).json()
  pages = response['data']['webfront_searchVideo']['pageInfo']['pages']

  titles = list()
  with ProcessPoolExecutor(10) as e:
    for result in e.map(getTitlesByPage, list(range(1, pages+1))):
      titles.extend(result)

  output_json = {
      'titles' : titles,
  }

  with open(f"./data/{jsonData['variables']['categoryCode']}.json", "w") as f: json.dump(output_json, f, ensure_ascii=False, indent=4)

def main():
  getTitlesByCategoryCode('MNU0000141')
  getTitlesByCategoryCode('MNU0000709')
  getTitlesByCategoryCode('MNU0000725')
  getTitlesByCategoryCode('MNU0000753')
  getTitlesByCategoryCode('MNU0000768')

if __name__ == '__main__':
    main()