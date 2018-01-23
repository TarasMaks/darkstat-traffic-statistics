import pandas as pd
import requests
from plotly.graph_objs import *
csv_folder = r'path\to\excel-export-folder'
csv_file = r'\excel export.csv'

def calculation(csv_folder, csv_file):
    page = 'http://darkstatIP/hosts/?full=yes&sort=total'
    main = requests.get(page)
    indicator = {'IP':[], 'Hostname':[], 'In':[], 'Out':[], 'Total':[], 'Last seen':[]}

    data = main.text
    splitlist = data.split('href=\"./')
    r = data.count("alt2")
    t = 1
    for s in range(r):
        first = (splitlist[t])
        temp1 = (first.split('</td>')[0])
        ip = (temp1.split('/')[0])
        temp2 = (first.split('</td>')[1])
        host = (temp2.split('>')[1])
        temp3 = (first.split('</td>')[3])
        inta = (temp3.split('>')[1])
        temp4 = (first.split('</td>')[4])
        outa = (temp4.split('>')[1])
        temp5 = (first.split('</td>')[5])
        totala = (temp5.split('>')[1])
        temp6 = (first.split('</td>')[6])
        lasa = (temp6.split('>')[1])
        t = t+1
        indicator['IP'].append(ip)
        indicator['Hostname'].append(host)
        indicator['In'].append(inta)
        indicator['Out'].append(outa)
        indicator['Total'].append(totala)
        indicator['Last seen'].append(lasa)


    myInt = 1000000000

    result = list(map(lambda x: int(x.replace(",", "")), indicator['Total']))
    result1 = list(map(lambda x: int(x.replace(",", "")), indicator['In']))
    result2 = list(map(lambda x: int(x.replace(",", "")), indicator['Out']))
    gblist = []
    inlist = []
    outlist = []
    for x in result:
        b = x / myInt
        gblist.append(b)
    for x in result1:
        c = x / myInt
        inlist.append(c)
    for x in result2:
        d = x / myInt
        outlist.append(d)
    indicator['Total'] = gblist
    indicator['In'] = inlist
    indicator['Out'] = outlist

    df = pd.DataFrame(indicator)
    df = df[df.Hostname.str[-3:]!= "box"]

    # Zeit in die Tabelle

    from time import strftime
    df['time'] = (strftime("%Y-%m-%d"))

    #export to excel

    df['In_MB'] = df['In'] * 1000
    df['Out_MB'] = df['Out'] * 1000
    df['Total_MB'] = df['Total'] * 1000
    df['In_TB'] = df['In'] / 1000
    df['Out_TB'] = df['Out'] / 1000
    df['Total_TB'] = df['Total'] / 1000

    df = df.round({'In': 3, 'Out':3, 'Total':3, 'In_MB':0, 'Out_MB': 0, 'Total_MB':0, 'In_TB': 3, 'Out_TB':3, 'Total_TB':3})

    print(df.head(10))

    dfa = df[['time','In_TB','Out_TB', 'Total_TB','In', 'Out', 'Total', 'In_MB', 'Out_MB', 'Total_MB']]
    #dfa.head(1).to_csv(csv_folder + csv_file, index=False)
    print(dfa.head(1))
    dfa.head(1).to_csv(csv_folder + csv_file, index=False, header=False, mode = 'a')
    return
def display(csv_folder, csv_file):
    from plotly.offline import plot

    df = pd.read_csv(csv_folder + csv_file)

    df['diff_In'] = df.In.diff()
    df['diff_Out'] = df.Out.diff()

    trace1 = Bar(
        x=df['time'],
        y=df['diff_In'],
        text=df['In'],
        name='GB In')
    trace2 = Bar(
        x=df['time'],
        y=df['diff_Out'],
        text=df['Out'],
        name='GB Out')

    data = [trace1, trace2]
    layout = Layout(barmode='stack', title='darkstat stats')

    fig = dict(data=data, layout=layout)
    plot(fig,filename= csv_folder + '\darkstat_stats.html', auto_open=False)
    print(trace1)
    return

calculation(csv_folder, csv_file)

display(csv_folder, csv_file)
