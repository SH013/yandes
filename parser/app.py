def find_realty_objects(csv_db):
    with open('twice_sold.csv', 'w') as answer:
        with open(csv_db, 'r') as database:
            adress_dict = {}

            for line in database:
                cols = line.strip().split(',')
                items = [cols[i] for i in range(6, 13)]
                if items[0] == '"F"':
                    adresse = ", ".join(items).replace('"', '').replace(',', '') + "\n"
                    print(adresse)
                    if adresse not in adress_dict:
                        adress_dict[adresse] = 1
                    elif adress_dict[adresse] == 1:
                        adress_dict[adresse] += 1
                        answer.write(adresse)
                    else:
                        continue


if __name__ == "__main__":
    find_realty_objects('pp-complete.csv')