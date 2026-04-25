def main():
    dataset = []
    with open('./cats-facts-rag.txt', 'r') as file:
      dataset = file.readlines()
      print(f'Loaded {len(dataset)} entries')



if __name__ == "__main__":
    main()
