import subprocess


def map_ports():
    with open("iplist.cnf", "r") as infile, open("output.csv", "w") as outfile:
        for line in infile:
            print(line.replace('\n', ''))
            line = line.replace('\n', '')
            subprocess.run(['nmap', '-Pn', line, '-oG', 'temp'])
            temp = open("temp", "r")
            lines = temp.readlines()
            base = ''
            if(lines[1].find('Status: Up') != -1):
                base = line + ',UP'
                print(line + ': Status UP')
                leng = len(lines[2].split('Ports: '))
                if(leng > 1):
                    ports = lines[2].split('Ports: ')[1].split(',')
                    for port in ports:
                        parsed_port = port.split('/')
                        output = base+',' + \
                            parsed_port[0].strip()+','+parsed_port[1]+',' + \
                            parsed_port[2]+','+parsed_port[4]+'\n'
                        outfile.write(output)
                        print(output)
                else:
                    base = line + ',UP'
                    output = base+'\n'
                    outfile.write(output)
                    print(output)

            else:
                base = line + ',DOWN'
                output = base+'\n'
                outfile.write(output)
                print(output)


map_ports()
