import datetime
import random
import time
import  datetime as dt

NAMES = ['Liam', 'Noah', 'Oliver', 'William', 'Elijah', 'James', 'Benjamin', 'Lucas', 'Mason', 'Ethan', 'Alexander', 'Henry', 'Jacob', 'Michael', 'Daniel', 'Logan', 'Jackson', 'Sebastian', 'Jack', 'Aiden', 'Owen', 'Samuel', 'Matthew', 'Joseph', 'Levi', 'Mateo', 'David', 'John', 'Wyatt', 'Carter', 'Julian', 'Luke', 'Grayson', 'Isaac', 'Jayden', 'Theodore', 'Gabriel', 'Anthony', 'Dylan', 'Leo', 'Lincoln', 'Jaxon', 'Asher', 'Christopher', 'Josiah', 'Andrew', 'Thomas', 'Joshua', 'Ezra', 'Hudson', 'Charles', 'Caleb', 'Isaiah', 'Ryan', 'Nathan', 'Adrian', 'Christian', 'Maverick', 'Colton', 'Elias', 'Aaron', 'Eli', 'Landon', 'Jonathan', 'Nolan', 'Hunter', 'Cameron', 'Connor', 'Santiago', 'Jeremiah', 'Ezekiel', 'Angel', 'Roman', 'Easton', 'Miles', 'Robert', 'Jameson', 'Nicholas', 'Greyson', 'Cooper', 'Ian', 'Carson', 'Axel', 'Jaxson', 'Dominic', 'Leonardo', 'Luca', 'Austin', 'Jordan', 'Adam', 'Xavier', 'Jose', 'Jace', 'Everett', 'Declan', 'Evan', 'Kayden', 'Parker', 'Wesley', 'Kai', 'Brayden', 'Bryson', 'Weston', 'Jason', 'Emmett', 'Sawyer', 'Silas', 'Bennett', 'Brooks', 'Micah', 'Damian', 'Harrison', 'Waylon', 'Ayden', 'Vincent', 'Ryder', 'Kingston', 'Rowan', 'George', 'Luis', 'Chase', 'Cole', 'Nathaniel', 'Zachary', 'Ashton', 'Braxton', 'Gavin', 'Tyler', 'Diego', 'Bentley', 'Amir', 'Beau', 'Gael', 'Carlos', 'Ryker', 'Jasper', 'Max', 'Juan', 'Ivan', 'Brandon', 'Jonah', 'Giovanni', 'Kaiden', 'Myles', 'Calvin', 'Lorenzo', 'Maxwell', 'Jayce', 'Kevin', 'Legend', 'Tristan', 'Jesus', 'Jude', 'Zion', 'Justin', 'Maddox', 'Abel', 'King', 'Camden', 'Elliott', 'Malachi', 'Milo', 'Emmanuel', 'Karter', 'Rhett', 'Alex', 'August', 'River', 'Xander', 'Antonio', 'Brody', 'Finn', 'Elliot', 'Dean', 'Emiliano', 'Eric', 'Miguel', 'Arthur', 'Matteo', 'Graham', 'Alan', 'Nicolas', 'Blake', 'Thiago', 'Adriel', 'Victor', 'Joel', 'Timothy', 'Hayden', 'Judah', 'Abraham', 'Edward', 'Messiah', 'Zayden', 'Theo', 'Tucker', 'Grant', 'Richard', 'Alejandro', 'Steven', 'Jesse', 'Dawson', 'Bryce', 'Avery', 'Oscar', 'Patrick', 'Archer', 'Barrett', 'Leon', 'Colt', 'Charlie', 'Peter', 'Kaleb', 'Lukas', 'Beckett', 'Jeremy', 'Preston', 'Enzo', 'Luka', 'Andres', 'Marcus', 'Felix', 'Mark', 'Ace', 'Brantley', 'Atlas', 'Remington', 'Maximus', 'Matias', 'Walker', 'Kyrie', 'Griffin', 'Kenneth', 'Israel', 'Javier', 'Kyler', 'Jax', 'Amari', 'Zane', 'Emilio', 'Knox', 'Adonis', 'Aidan', 'Kaden', 'Paul', 'Omar', 'Brian', 'Louis', 'Caden', 'Maximiliano', 'Holden', 'Paxton', 'Nash', 'Bradley', 'Bryan', 'Simon', 'Phoenix', 'Lane', 'Josue', 'Colin', 'Rafael', 'Kyle', 'Riley', 'Jorge', 'Beckham', 'Cayden', 'Jaden', 'Emerson', 'Ronan', 'Karson', 'Arlo', 'Tobias', 'Brady', 'Clayton', 'Francisco', 'Zander', 'Erick', 'Walter', 'Daxton', 'Cash', 'Martin', 'Damien', 'Dallas', 'Cody', 'Chance', 'Jensen', 'Finley', 'Jett', 'Corbin', 'Kash', 'Reid', 'Kameron', 'Andre', 'Gunner', 'Jake', 'Hayes', 'Manuel', 'Prince', 'Bodhi', 'Cohen', 'Sean', 'Khalil', 'Hendrix', 'Derek', 'Cristian', 'Cruz', 'Kairo', 'Dante', 'Atticus', 'Killian', 'Stephen', 'Orion', 'Malakai', 'Ali', 'Eduardo', 'Fernando', 'Anderson', 'Angelo', 'Spencer', 'Gideon', 'Mario', 'Titus', 'Travis', 'Rylan', 'Kayson', 'Ricardo', 'Tanner', 'Malcolm', 'Raymond', 'Odin', 'Cesar', 'Lennox', 'Joaquin', 'Kane', 'Wade', 'Muhammad', 'Iker', 'Jaylen', 'Crew', 'Zayn', 'Hector', 'Ellis', 'Leonel', 'Cairo', 'Garrett', 'Romeo', 'Dakota', 'Edwin', 'Warren', 'Julius', 'Major', 'Donovan', 'Caiden', 'Tyson', 'Nico', 'Sergio', 'Nasir', 'Rory', 'Devin', 'Jaiden', 'Jared', 'Kason', 'Malik', 'Jeffrey', 'Ismael', 'Elian', 'Marshall', 'Lawson', 'Desmond', 'Winston', 'Nehemiah', 'Ari', 'Conner', 'Jay', 'Kade', 'Andy', 'Johnny', 'Jayceon', 'Marco', 'Seth', 'Ibrahim', 'Raiden', 'Collin', 'Edgar', 'Erik', 'Troy', 'Clark', 'Jaxton', 'Johnathan', 'Gregory', 'Russell', 'Royce', 'Fabian', 'Ezequiel', 'Noel', 'Pablo', 'Cade', 'Pedro', 'Sullivan', 'Trevor', 'Reed', 'Quinn', 'Frank', 'Harvey', 'Princeton', 'Zayne', 'Matthias', 'Conor', 'Sterling', 'Dax', 'Grady', 'Cyrus', 'Gage', 'Leland', 'Solomon', 'Emanuel', 'Niko', 'Ruben', 'Kasen', 'Mathias', 'Kashton', 'Franklin', 'Remy', 'Shane', 'Kendrick', 'Shawn', 'Otto', 'Armani', 'Keegan', 'Finnegan', 'Memphis', 'Bowen', 'Dominick', 'Kolton', 'Jamison', 'Allen', 'Philip', 'Tate', 'Peyton', 'Jase', 'Oakley', 'Rhys', 'Kyson', 'Adan', 'Esteban', 'Dalton', 'Gianni', 'Callum', 'Sage', 'Alexis', 'Milan', 'Moises', 'Jonas', 'Uriel', 'Colson', 'Marcos', 'Zaiden', 'Hank', 'Damon', 'Hugo', 'Ronin', 'Royal', 'Kamden', 'Dexter', 'Luciano', 'Alonzo', 'Augustus', 'Kamari', 'Eden', 'Roberto', 'Baker', 'Bruce', 'Kian', 'Albert', 'Frederick', 'Mohamed', 'Abram', 'Omari', 'Porter', 'Enrique', 'Alijah', 'Francis', 'Leonidas', 'Zachariah', 'Landen', 'Wilder', 'Apollo', 'Santino', 'Tatum', 'Pierce', 'Forrest', 'Corey', 'Derrick', 'Isaias', 'Kaison', 'Kieran', 'Arjun', 'Gunnar', 'Rocco', 'Emmitt', 'Abdiel', 'Braylen', 'Maximilian', 'Skyler', 'Phillip', 'Benson', 'Cannon', 'Deacon', 'Dorian', 'Asa', 'Moses', 'Ayaan', 'Jayson', 'Raul', 'Briggs', 'Armando', 'Nikolai', 'Cassius', 'Drew', 'Rodrigo', 'Raphael', 'Danny', 'Conrad', 'Moshe', 'Zyaire', 'Julio', 'Casey', 'Ronald', 'Scott', 'Callan', 'Roland', 'Saul', 'Jalen', 'Brycen', 'Ryland', 'Lawrence', 'Davis', 'Rowen', 'Zain', 'Ermias', 'Jaime', 'Duke', 'Stetson', 'Alec', 'Yusuf', 'Case', 'Trenton', 'Callen', 'Ariel', 'Jasiah', 'Soren', 'Dennis', 'Donald', 'Keith', 'Izaiah', 'Lewis', 'Kylan', 'Kobe', 'Makai', 'Rayan', 'Ford', 'Zaire', 'Landyn', 'Roy', 'Bo', 'Chris', 'Jamari', 'Ares', 'Mohammad', 'Darius', 'Drake', 'Tripp', 'Marcelo', 'Samson', 'Dustin', 'Layton', 'Gerardo', 'Johan', 'Kaysen', 'Keaton', 'Reece', 'Chandler', 'Lucca', 'Mack', 'Baylor', 'Kannon', 'Marvin', 'Huxley', 'Nixon', 'Tony', 'Cason', 'Mauricio', 'Quentin', 'Edison', 'Quincy', 'Ahmed', 'Finnley', 'Justice', 'Taylor', 'Gustavo', 'Brock', 'Ahmad', 'Kyree', 'Arturo', 'Nikolas', 'Boston', 'Sincere', 'Alessandro', 'Braylon', 'Colby', 'Leonard', 'Ridge', 'Trey', 'Aden', 'Leandro', 'Sam', 'Uriah', 'Ty', 'Sylas', 'Axton', 'Issac', 'Fletcher', 'Julien', 'Wells', 'Alden', 'Vihaan', 'Jamir', 'Valentino', 'Shepherd', 'Keanu', 'Hezekiah', 'Lionel', 'Kohen', 'Zaid', 'Alberto', 'Neil', 'Denver', 'Aarav', 'Brendan', 'Dillon', 'Koda', 'Sutton', 'Kingsley', 'Sonny', 'Alfredo', 'Wilson', 'Harry', 'Jaziel', 'Salvador', 'Cullen', 'Hamza', 'Dariel', 'Rex', 'Zeke', 'Mohammed', 'Nelson', 'Boone', 'Ricky', 'Santana', 'Cayson', 'Lance', 'Raylan', 'Lucian', 'Eliel', 'Alvin', 'Jagger', 'Braden', 'Curtis', 'Mathew', 'Jimmy', 'Kareem', 'Archie', 'Amos', 'Quinton', 'Yosef', 'Bodie', 'Jerry', 'Langston', 'Axl', 'Stanley', 'Clay', 'Douglas', 'Layne', 'Titan', 'Tomas', 'Houston', 'Darren', 'Lachlan', 'Kase', 'Korbin', 'Leighton', 'Joziah', 'Samir', 'Watson', 'Colten', 'Roger', 'Shiloh', 'Tommy', 'Mitchell', 'Azariah', 'Noe', 'Talon', 'Deandre', 'Lochlan', 'Joe', 'Carmelo', 'Otis', 'Randy', 'Byron', 'Chaim', 'Lennon', 'Devon', 'Nathanael', 'Bruno', 'Aryan', 'Flynn', 'Vicente', 'Brixton', 'Kyro', 'Brennan', 'Casen', 'Kenzo', 'Orlando', 'Castiel', 'Rayden', 'Ben', 'Grey', 'Jedidiah', 'Tadeo', 'Morgan', 'Augustine', 'Mekhi', 'Abdullah', 'Ramon', 'Saint', 'Emery', 'Maurice', 'Jefferson', 'Maximo', 'Koa', 'Ray', 'Jamie', 'Eddie', 'Guillermo', 'Onyx', 'Thaddeus', 'Wayne', 'Hassan', 'Alonso', 'Dash', 'Elisha', 'Jaxxon', 'Rohan', 'Carl', 'Kelvin', 'Jon', 'Larry', 'Reese', 'Aldo', 'Marcel', 'Melvin', 'Yousef', 'Aron', 'Kace', 'Vincenzo', 'Kellan', 'Miller', 'Jakob', 'Reign', 'Kellen', 'Kristopher', 'Ernesto', 'Briar', 'Gary', 'Trace', 'Joey', 'Clyde', 'Enoch', 'Jaxx', 'Crosby', 'Magnus', 'Fisher', 'Jadiel', 'Bronson', 'Eugene', 'Lee', 'Brecken', 'Atreus', 'Madden', 'Khari', 'Caspian', 'Ishaan', 'Kristian', 'Westley', 'Hugh', 'Kamryn', 'Musa', 'Rey', 'Thatcher', 'Alfred', 'Emory', 'Kye', 'Reyansh', 'Yahir', 'Cain', 'Mordechai', 'Zayd', 'Demetrius', 'Harley', 'Felipe', 'Louie', 'Branson', 'Graysen', 'Allan', 'Kole', 'Harold', 'Alvaro', 'Harlan', 'Amias', 'Brett', 'Khalid', 'Misael', 'Westin', 'Zechariah', 'Aydin', 'Kaiser', 'Lian', 'Bryant', 'Junior', 'Legacy', 'Ulises', 'Bellamy', 'Brayan', 'Kody', 'Ledger', 'Eliseo', 'Gordon', 'London', 'Rocky', 'Valentin', 'Terry', 'Damari', 'Trent', 'Bentlee', 'Canaan', 'Gatlin', 'Kiaan', 'Franco', 'Eithan', 'Idris', 'Krew', 'Yehuda', 'Marlon', 'Rodney', 'Creed', 'Salvatore', 'Stefan', 'Tristen', 'Adrien', 'Jamal', 'Judson', 'Camilo', 'Kenny', 'Nova', 'Robin', 'Rudy', 'Van', 'Bjorn', 'Brodie', 'Mac', 'Jacoby', 'Sekani', 'Vivaan', 'Blaine', 'Ira', 'Ameer', 'Dominik', 'Alaric', 'Dane', 'Jeremias', 'Kyng', 'Reginald', 'Bobby', 'Kabir', 'Jairo', 'Alexzander', 'Benicio', 'Vance', 'Wallace', 'Zavier', 'Billy', 'Callahan', 'Dakari', 'Gerald', 'Turner', 'Bear', 'Jabari', 'Cory', 'Fox', 'Harlem', 'Jakari', 'Jeffery', 'Maxton', 'Ronnie', 'Yisroel', 'Zakai', 'Bridger', 'Remi', 'Arian', 'Blaze', 'Forest', 'Genesis', 'Jerome', 'Reuben', 'Wesson', 'Anders', 'Banks', 'Calum', 'Dayton', 'Kylen', 'Dangelo', 'Emir', 'Malakhi', 'Salem', 'Blaise', 'Tru', 'Boden', 'Kolten', 'Kylo', 'Aries', 'Henrik', 'Kalel', 'Landry', 'Marcellus', 'Zahir', 'Lyle', 'Dario', 'Rene', 'Terrance', 'Xzavier', 'Alfonso', 'Darian', 'Kylian', 'Maison', 'Foster', 'Keenan', 'Yahya', 'Heath', 'Javion', 'Jericho', 'Aziel', 'Darwin', 'Marquis', 'Mylo', 'Ambrose', 'Anakin', 'Jordy', 'Juelz', 'Toby', 'Yael', 'Azrael', 'Brentley', 'Tristian', 'Bode', 'Jovanni', 'Santos', 'Alistair', 'Braydon', 'Kamdyn', 'Marc', 'Mayson', 'Niklaus', 'Simeon', 'Colter', 'Davion', 'Leroy', 'Ayan', 'Dilan', 'Ephraim', 'Anson', 'Merrick', 'Wes', 'Will', 'Jaxen', 'Maxim', 'Howard', 'Jad', 'Jesiah', 'Ignacio', 'Zyon', 'Ahmir', 'Jair', 'Mustafa', 'Jermaine', 'Yadiel', 'Aayan', 'Dhruv', 'Seven', 'Stone', 'Rome']
COUNTRIES = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Côte', 'Cabo', 'Cambodia', 'Cameroon', 'Canada', 'Central', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa', 'Croatia', 'Cuba', 'Cyprus', 'Czechia', 'Democratic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican', 'Ecuador', 'Egypt', 'El', 'Equatorial', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea', 'Guyana', 'Haiti', 'Holy', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New', 'Nicaragua', 'Niger', 'Nigeria', 'North', 'North', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint', 'Saint', 'Saint', 'Samoa', 'San', 'Sao', 'Saudi', 'Senegal', 'Serbia', 'Seychelles', 'Sierra', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon', 'Somalia', 'South', 'South', 'South', 'Spain', 'Sri', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United', 'United', 'United', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
TARGETS = ['recreation', 'tourism', 'treatment', 'work']
USERS = {}
SCHEMA_NAME = 'public'


def gen_users(pasport_id_length=5, uniq_names=False):
    """
    :param pasport_id_length: string with digit in range 10^(pasport_id_length-1):(10^pasport_id_length)-1
    :param uniq_names: If true the name will be deleted after first using
    :return: 
    """
    pass_id = [i for i in range(pow(10, pasport_id_length-1), pow(10, pasport_id_length)-1)]
    # print(pass_id)

    for i in range(len(pass_id)):
        name_id = random.randrange(len(NAMES)-1)
        USERS.setdefault(pass_id[random.randrange(0, len(pass_id)-1)], NAMES[name_id])
        if uniq_names:
            NAMES.remove(NAMES[name_id])

    # print(USERS)
    user_string = ""
    for pass_id, name in USERS.items():
        user_string += f"INSERT INTO {SCHEMA_NAME}.users VALUES('{pass_id}','{name}');COMMIT;\n"

    return user_string[:-2]+";"


def gen_paths():

    path_string = ""
    for country in COUNTRIES:
        path_string += f"INSERT INTO {SCHEMA_NAME}.paths (country, price_visa, price_day, price_transport) VALUES \n"\
                       f"\t('{country}',{random.randrange(1,10)*1000},{random.randrange(1,10)*100}," \
                       f"{random.randrange(1,10)*100+50});COMMIT;\n"
    # print(path_string)
    return path_string[:-2]+";"

    # s_countries = random.shuffle(COUNTRIES)


def gen_travels():
    def str_time_prop(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)

        return time.strftime(format, time.localtime(ptime))

    def random_date(start, end, prop):
        return str_time_prop(start, end, '%Y-%m-%d', prop)


    travel_string = ""
    for pass_id, name in USERS.items():
        for i in range(random.randrange(1, 10)):
            rnd_date = random_date("2021-01-01", "2050-12-31", random.random())
            travel_string += f"INSERT INTO {SCHEMA_NAME}.travels (path_id, user_passport, started_date, days_count, travel_target) VALUES \n"\
                             f"\t({random.randrange(1,len(COUNTRIES)-1)},'{pass_id}'," \
                             f"'{rnd_date}'," \
                             f"{random.randrange(1,365)},'{TARGETS[random.randrange(0,len(TARGETS)-1)]}');COMMIT;\n"
    # print(travel_string)
    return travel_string[:-2]+";"


def main():
    length = 1
    sql = f"{gen_users(length)}\n\n{gen_paths()}\n\n{gen_travels()}"
    with open('data.sql', 'w', encoding='utf-8') as f:
        f.write(sql)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    diff = "{:.4f}".format(float(end - start))
    print(f"SEC:{diff}")
