import pickle


def decryption(path:str) -> print:
    with open(path, 'rb') as file:
        loaded = pickle.load(file)
        for i in loaded:
            res = str()
            for j in i:
                res += j[0]*j[1]
            print(res)

decryption('problem_6.pkl')
# channel