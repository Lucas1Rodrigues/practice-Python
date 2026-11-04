from classes import *
def main():
    f1 = Gerente("Lucas",5000)
    print(f1)
    f2 = Desenvolvedor("Lucas",1000)
    print(f2)
    try:
        f2.salario = 200
    except Exception as e: 
        print(f"Aconteceu um erro tipo: {e}")
    
if __name__ == "__main__":
    main()