#!/usr/bin/env python

from .app import App

def main():
    app = App() 
    app.ask_user_input_data()
    app.fetch_data()
    app.generate_report()
        
if __name__ == '__main__':
    main()
