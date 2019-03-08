"""
Copyright (C) 2019 Jack Lansdale

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
life = [20]

#print('\x1b[0;31;40m' + 'Buffer Overflow Error: value too large to store in unsigned byte' + '\x1b[0m')

print('\x1b[0;25;5m' + 'life counter = ' + str(life[0]) + '\x1b[0m' )


def do_thing():
    print('\x1b[31;40;0m' + " select life change" + "\x1b[0m" )
    print('\x1b[0;31;40m' + " gain or loss" + "\x1b[0m" )
    selection = input()
    if selection == "gain":
        print("'\x1b[255;255;255' + Input how much life you gain" + "\x1b[m0" )
        x = int(input())
        y = life[0] + x
        life.clear()
        life.append(y)
        do_thing()
    elif selection == "loss":
        print("input  how much life you lose")
        x = int(input())
        y = life[0] - x
        life.clear()
        life.append(y)
        do_thing()
    else:
        print("you must enter \"gain\" or \"loss\"")
        do_thing()


do_thing()
