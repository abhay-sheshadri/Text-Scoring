import model
import dill

def main():
    while True:
        # Load model
        with open(r"training/model.dill", 'rb') as file:
            model = dill.load(file)
        # Start rating!
        sent = input("Enter a sentence: ")
        if sent != '':
            print("Score: {}/10".format(model.rate(sent)))

if __name__ == '__main__':
    main()
