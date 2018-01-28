#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5) # ID =0, FORENAME = 1, ...

User = collections.namedtuple("User",
            "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file: # each line > id:forename:middlename:surname:job\n
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
                    # users[key] = value
                    # key = (user.surname.lower(), user.forename.lower(), user.id)
                    # value = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    print_users(users)


def process_line(line, usernames):
    fields = line.split(":") # [id, forename, middlename, lastname]
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", "")) 
    # username = first character of FORENAME + first character of MIDDLEname + SURNAME
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    # usernames = set()
    return username


def print_users(users):
    namewidth = 17
    usernamewidth = 9

    users_list = sorted(users) # list of namedtuples
    loop_count = 1
    for key_l, key_r in zip(users_list[0::2], users_list[1::2]):
        user_l = users[key_l]
        user_r = users[key_r]

        if loop_count == 1:
            print("{0:<{nw}} {1:^6} {2:{uw}}  {0:<{nw}} {1:^6} {2:{uw}}".format(
                "Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
            print("{0:-<{nw}} {0:-<6} {0:-<{uw}}  {0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
                "", nw=namewidth, uw=usernamewidth))
        elif loop_count % 64 == 0:
            print("\n{0:-^70}".format("Fim da Página"), end='\n\n')
            print("{0:<{nw}} {1:^6} {2:{uw}}  {0:<{nw}} {1:^6} {2:{uw}}".format(
                "Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
            print("{0:-<{nw}} {0:-<6} {0:-<{uw}}  {0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
                "", nw=namewidth, uw=usernamewidth))

        initial_l = ""
        if user_l.middlename:
            initial_l = " " + user_l.middlename[0]

        name_l = "{0.surname}, {0.forename}{1}".format(user_l, initial_l)

        initial_r = ""
        if user_r.middlename:
            
            initial_r = " " + user_r.middlename[0]

        name_r = "{0.surname}, {0.forename}{1}".format(user_r, initial_r)

        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}  {2:.<{nw}} ({3.id:4}) {3.username:{uw}}".format(
            name_l[:16], user_l, name_r[:16], user_r, nw=namewidth, uw=usernamewidth))
        
        loop_count += 1

        


main()

"""
for key in sorted(users): # sorts them by the key.
        # key = (user.surname.lower(), user.forename.lower(), user.id)
        # value = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        # name = user.surname + user.forname + initial (" " + first middlename character)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
              name, user, nw=namewidth, uw=usernamewidth))
"""