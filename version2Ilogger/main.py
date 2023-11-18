from ilogger.ilogger import ILogger

def main():
    # Simulation d'un message d'erreur
    try:
        # Code qui pourrait générer une erreur
        raise ValueError("Ceci est un message d'erreur simulé.")
    except ValueError as e:
        ILogger.log(str(e), "ERROR")

    # Simulation d'un message d'avertissement
    ILogger.log("Ceci est un message d'avertissement simulé.", "WARNING")

if __name__ == '__main__':
    main()
