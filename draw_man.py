def draw_man(incorrect_count):

    if incorrect_count == 1:
        man = """
             ╔═══════╗
             ║       O 
             ║
             ║
             ║
             ║
           ══╝══
        """

    elif incorrect_count == 2:
        man = """
             ╔═══════╗
             ║       O 
             ║       |
             ║       |
             ║
             ║
           ══╝══
        """

    elif incorrect_count == 3:
        man = """
             ╔═══════╗
             ║       O 
             ║      \\|
             ║       |
             ║
             ║
           ══╝══
        """
    elif incorrect_count == 4:
        man = """
             ╔═══════╗
             ║       O 
             ║      \\|/
             ║       |
             ║
             ║
           ══╝══
        """

    elif incorrect_count == 5:
        man = """
             ╔═══════╗
             ║       O 
             ║      \\|/
             ║       |
             ║      / 
             ║
           ══╝══
        """
    elif incorrect_count == 6:
        man = """
             ╔═══════╗
             ║       O 
             ║      \\|/
             ║       |
             ║      / \\
             ║
           ══╝══
        """

    print(man)