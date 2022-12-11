import deepl

auth_key = "aafef425-e593-f5a5-90c2-74d7b067cfe1:fx"
t = deepl.Translator(auth_key)


def trans(str, fro, to):
    return t.translate_text(str, source_lang=fro, target_lang=to)


print("Input \'r\' to reverse the language or \'e\' to exit.\n")
nltoen = True
while True:
    with open('mywords.txt', 'a') as f:
        if nltoen:
            inp = input("Dutch -> English:  ")
            out = trans(inp, 'NL', 'EN-GB')
        else:
            inp = input("English -> Dutch:  ")
            out = trans(inp, 'EN', 'NL')
        if inp == 'r':
            nltoen = not nltoen
            print('')
            continue
        if inp == 'e':
            break
        print(f"Translation:       {out}\n")
        if nltoen:
            f.write(f"{inp},{out}\n")
        else:
            f.write(f"{out},{inp}\n")
