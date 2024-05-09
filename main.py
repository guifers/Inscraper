import argparse
from scraping.scraping_module import scrape_instagram
from filewriter.file_writer import verify_folder

def main():
    parser = argparse.ArgumentParser(description='Descripción de tu aplicación')
    parser.add_argument('user_to_scrape', type=str, help='Usuario a realizar el scraping')
    parser.add_argument('user', type=str, help='Tu usuario de instagram')
    parser.add_argument('pw', type=str, help='Tu contraseña')
    args = parser.parse_args()

    print("Opcion:", args.user_to_scrape)
    print(args.user_to_scrape)
    if verify_folder('a', args.user_to_scrape)!=0:
        print("El usuario no está entre sus registros.Añadiendo usuario y realizando primer escaneo...")
        scrape_instagram(args.user_to_scrape, args.user, args.pw)
    else:
        scrape_instagram(args.user_to_scrape, args.user, args.pw)


if __name__ == '__main__':
    main()
