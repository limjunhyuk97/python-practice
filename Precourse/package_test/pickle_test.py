import pickle

data = {
    "objective1" : "crawling data from ajou portal",
    "objective2" : "making database"
}

# 1. with 이용하여 pickle file에 데이터 저장하기
with open("../by-product/data.pickle", "wb") as file:
    # file 객체로 data를 dump한다.
    pickle.dump(data, file)

# 2. with 이용하여 pickle file 열기
with open("../by-product/data.pickle", "rb") as file:
    # file 객체 내부의 binary 정보를 load한다.
    loaded = pickle.load(file)
    print(loaded)