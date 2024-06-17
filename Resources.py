import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

Dream_Piece_Locations_Fail = "https://www.ign.com/wikis/kingdom-hearts-3d-dream-drop-distance/Dream_Piece_Locations"
    #Don't use IGN because they don't like it. 
Dream_Piece_Locations = "https://samurai-gamers.com/kingdom-hearts-3/dream-pieces-locations-kh-2-8/"
Spirit_Recipes = "https://strategywiki.org/wiki/Kingdom_Hearts_3D:_Dream_Drop_Distance/Recipes"
Dream_Eater_Locations = "https://strategywiki.org/wiki/Kingdom_Hearts_3D:_Dream_Drop_Distance/Dream_Eaters"

SPIRIT_RECIPES = [
    {
        "Spirit": "Aura Lion",
        "Rank": "D",
        "Material 1": (3,"Intrepid Fantasy"),
        "Material 2": (3,"Noble Fantasy"),
        "Success": "100%"
    },
]
def make_spirit_recipes_json():
    SPIRIT_RECIPES = []
    page = requests.get(Spirit_Recipes)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    headings = [heading.text.strip() for heading in table.find('tr').find_all('th')]
    category = 'normal'
    for row in rows[1:]:
        row_info = {}
        columns = row.find_all('td')
        if not columns:
            category:str = row.find('th').text.strip()
            continue
        if category == 'AR (3DS only)':
            continue #might fix later but for now I want to just skip unusable for me
        if len(columns) == 5:
            share_info = columns[0].text.strip()
        for num,column in enumerate(columns):
            if len(columns) == 4:
                if num == 0:
                    row_info[headings[0]] = share_info
                num += 1
            row_info[headings[num]] = column.text.strip()
        if not row_info:
            continue #if there in no info in that 
        SPIRIT_RECIPES.append(row_info)
    with open('SpiritRecipies.json','w') as file:
        json.dump(SPIRIT_RECIPES,file)

DREAM_PIECE_ENCYCLOPEDIA = {
    'Intrepid Fantasy':{
        'Spirit':[
            'Aura Lion',
        ],
        'Moogle Shop':{
            'Sale Day':True,
            'Munny':800
        }
    }
}

def make_dream_piece_encyclopedia_json():
    DREAM_PIECE_ENCYCLOPEDIA = []
    page = requests.get(Dream_Piece_Locations)
    soup = BeautifulSoup(page.content,'html.parser')
    tables = soup.find_all('table')
    MoogleShopTable = tables[0]
    SpiritsTable = tables[1]
    
    DPE_pt1 = {}
    def dream_piece_encyclopedia_part_1():
        #Setting up spirits
        rows = SpiritsTable.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            Dream_Eater_Name = columns[0].text
            Drops = columns[1].text.split('\n')
            DPE_pt1[Dream_Eater_Name] = Drops
    
    def dream_piece_encyclopedia_part_2():
        #Setting up Munny Shop
        rows = MoogleShopTable.find_all('tr')
        for row in rows[1:2]:
            if row.find_all('td') != 5:
                continue
            item_name = row.find_all('td')[0].text


    
    dream_piece_encyclopedia_part_2()
    


DREAM_EATER_ENCYCLOPEDIA = {
    "Aura Lion": {
        'Dream Pieces': [
            'Intrepid Fantasy',
            'Intrepid Fancy',
        ],
        'Locations':[
            'Country of the Musketeers'
        ]
    }
}

if __name__ == '__main__':
    make_dream_piece_encyclopedia_json()