import sys
class invalidlogin(Exception):
    pass
class Main:
    #stat=False
    def run_db(self):
        import DB_Connection
        DB = DB_Connection.DB_Access()
        DB.main_screen()
        self.stat = DB.return_status() #value return

    def run_Router_Packet_Details(self):
        try:
            if self.stat:
                import Router_Packet_Details
            else:
                raise invalidlogin
        except:
            sys.exit("please login, to access router_packet_details")
    def run_Ping_monitoring(self):
        try:
            if self.stat:
                import Ping_monitoring
            else:
                raise invalidlogin
        except:
            sys.exit("please login, to access ping_monitoring")
    def get_bandwidth(self):
        try:
            if self.stat:
                import Bandwidths
            else:
                raise invalidlogin
        except:
            sys.exit("please login, to access get_bandwidth")
    def port_finding(self):
        try:
            if self.stat:
                import finding_port
            else:
                raise invalidlogin
        except:
            sys.exit("please login, to access port_finding")
    def M_D_P(self):
        try:
            if self.stat:
                import MDP
            else:
                raise invalidlogin
        except:
            sys.exit("please login, to access router_packet_details")

def exitprogram():
    sys.exit("system exiting")
def printerror():
    print("Invalid option entered")
main = Main()

def run():
    menu = {
        1: main.run_db,
        2: main.run_Router_Packet_Details,
        3: main.run_Ping_monitoring,
        4: main.get_bandwidth,
        5: main.port_finding,
        6: main.M_D_P,
        7: exitprogram
    }
    while True:
        print(
            "\n 1:Establish DataBase connection\n2:Get router packet details"
            "\n3:Ping Monitoring\n4:Get Bandwidth\n5:port finding"
            "\n6:MDP\n7:Exit Program\nEnter your choice?",
            end='')
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a valid input!")
        menu.get(choice,printerror)()


# start
run()