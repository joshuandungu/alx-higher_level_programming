#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_hidden_names = dir(hidden_4)

    for i in range(len(def_hidden_names)):
        if def_hidden_names[i][:2] != '__':
            print(def_hidden_names[i])
