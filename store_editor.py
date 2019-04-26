import pickle


def pre_load():
    pre_load_store = {}
    for i in range(1, 10):
        pre_load_store[i] = "url:%d" % i
    with open('store.pkl', 'wb') as pre_load_f:
        pickle.dump(pre_load_store, pre_load_f, pickle.HIGHEST_PROTOCOL)


# pre_load()
store = {}

try:
    with open('store.pkl', 'rb') as f:
        store = pickle.load(f)
except FileNotFoundError:
    print("No existing store so preloading")
    pre_load()
    with open('store.pkl', 'rb') as f:
        store = pickle.load(f)

for key in store:
    print("%s: %s" % (key, store[key]))

command = ""
while not command == "q":
    raw = input(">> ")
    tokens = raw.split()

    if len(tokens) <= 0:
        continue

    command = tokens[0]

    if command == "d":
        if not len(tokens) == 2:
            print("Usage: d <id>")
            continue

        url_id = tokens[1]

        store = {k: v for k, v in store.items() if k != url_id}

    elif command == "p":
        for key in store:
            print("%s: %s" % (key, store[key]))

with open('store.pkl', 'wb') as f:
    pickle.dump(store, f, pickle.HIGHEST_PROTOCOL)
