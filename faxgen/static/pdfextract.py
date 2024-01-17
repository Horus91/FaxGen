from pypdf import PdfReader
from pathlib import Path
from datetime import datetime,timedelta
from docx import Document

OFPS_DIR= Path(__file__).resolve().parent.parent.joinpath('media').joinpath('ofps')
FXTEMP= Path(__file__).resolve().parent.parent.joinpath('static').joinpath('fxtemp.docx')


class Fax_elts():
    def __init__(self, fileurl):
        self.file=fileurl
        reader=PdfReader(fileurl)
        self.pages=reader.pages
        self.garde=reader.pages[0].extract_text()
        self.first=reader.pages[1].extract_text()

        # -----------Time Properties----------------
        self.datetime_dep=datetime.strptime(self.first[198:205]+self.first[676:680],'%d%b%y%H%M')
        self.trip_time= timedelta(hours=int(self.first[1267:1269]),minutes=int(self.first[1270:1272]))
        self.datetime_arr=self.datetime_dep+self.trip_time
        # ------------------------------------------

    def __str__(self):
        return f"{self.datetime_dep}, {self.datetime_arr}, {self.trip_time}"

    def general_infos(self):
        reg_marks=self.first[655:660]
        callsign=self.garde[14:21]
        origin=self.first[759:786]
        destination=self.first[829:856]
        alt1=self.first[899:926]
        alt2=self.first[969:996]
        return reg_marks,callsign,origin,destination,alt1,alt2
    
    def firs_extraction(self):
        for page in self.pages:
            e_page=page.extract_text()
            if '(FPL-' in e_page:
                firs=e_page[e_page.index('EET/')+4: e_page.index('SEL/')-1].split(' ')
                firs_lst=[]
                firs_timing=[]
                for fir in firs:
                    firs_lst.append(fir[:4])
                    firs_timing.append(fir[4:8])
                global last_log_page
                last_log_page=page.page_number

                return firs_lst,firs_timing
        
    def route_extraction(self):
        for page in self.pages:
            if 'ATC ROUTING:' in page.extract_text():
                atc_id=page.extract_text().find('ATC ROUTING:')
                rvsm_id=page.extract_text().find('RVSM')

                return page.extract_text()[atc_id+18:rvsm_id-75].replace("\n"," ")
            
# a=Fax_elts(fileurl=OFPS_DIR.joinpath('FlightPlan_K5461.pdf'))

# print(a.general_infos(), a.route_extraction(),a.firs_extraction(), a.datetime_arr.date())
# print( list(x for x in a.firs_extraction()[1]))
# print(a.first[655:660])
            

class Fax_docx():
    # def __init__(self,countries,ac_type,captain,Fax_elts):
    def __init__(self,Fax_elts):
        self.fax_template=Document(FXTEMP)
        # self.countries= countries
        # self.ac_type=ac_type
        # self.captain=captain
        self.Fax_elts=Fax_elts

    def generate_fax(self):
        # Cells positions {'5':pays survoles, '17':nbre type d'avion, '34': callsign, '34':registration, '53':Captain
        # , '120':Depdate,'125':etd,'122':Dep_airport,,'127':Arr_airport, '129':eta, '131':route,
        #  }
        table=self.fax_template.tables[0]
        table1=self.fax_template.tables[0]._cells[159].tables[0]
        
        
        # General Infos Respectively (reg;callsign;origin;destination)
        table._cells[34].text = self.Fax_elts.general_infos()[0]
        table._cells[24].text = self.Fax_elts.general_infos()[1]
        table._cells[122].text = self.Fax_elts.general_infos()[2]
        table._cells[127].text = self.Fax_elts.general_infos()[3]

        # Date Times 
        table._cells[120].text = self.Fax_elts.datetime_dep.strftime("%d%b%Y")
        table._cells[125].text = self.Fax_elts.datetime_dep.strftime("%H:%M GMT")
        table._cells[129].text = self.Fax_elts.datetime_arr.strftime("%H:%M GMT\n%d%b%Y")

        # Route:
        table._cells[131].text = self.Fax_elts.route_extraction()
        
        # FIRS:
        row_firs=table.rows[-1]
        firs_extracted=self.Fax_elts.firs_extraction()[0]
        firs_etos=self.Fax_elts.firs_extraction()[1]
        a=0
        for elt in range(len(firs_extracted)):
            a+=1
            table.add_row()._tr.addnext(row_firs._tr)
            table.rows[14+a].cells[0].merge(table.rows[14+a].cells[2])
            table.rows[14+a].cells[3].merge(table.rows[14+a].cells[7])
            table.rows[14+a].cells[8].merge(table.rows[14+a].cells[9])
            table.rows[14+a].cells[0].text=firs_extracted[elt]
            table.rows[14+a].cells[8].text=f"H+ {firs_etos[elt]}"
        
        # ALTERNATES:
            table1._cells[1].text=self.Fax_elts.general_infos()[4]
            table1._cells[3].text=self.Fax_elts.general_infos()[5]
        
        return self.fax_template.save(OFPS_DIR.joinpath('new.docx'))

        
        
b=Fax_docx(Fax_elts(OFPS_DIR.joinpath('FlightPlan_K5461.pdf')))
b.generate_fax()
    


# t=['a','b','c','d']
new_fax=Document(FXTEMP)
table= new_fax.tables[0]._cells[159].tables[0]
print(table._cells[3].text)


# row_firs=table.rows[-1]
# a=0
# for elt in range(len(t)):
#     a+=1
#     table.add_row()._tr.addnext(row_firs._tr)
#     table.rows[14+a].cells[0].merge(table.rows[14+a].cells[2])
#     table.rows[14+a].cells[3].merge(table.rows[14+a].cells[7])
#     table.rows[14+a].cells[8].merge(table.rows[14+a].cells[9])
#     table.rows[14+a].cells[0].text=t[elt]

# # print(table.rows[14].cells[9].text)
# new_fax.save(OFPS_DIR.joinpath('test.docx'))



# reader = PdfReader(OFPS_DIR.joinpath('FlightPlan_K5461.pdf'))



# pages=reader.pages
# garde=reader.pages[0].extract_text()
# first=reader.pages[1].extract_text()
    

# datetime_dep=datetime.strptime(first[198:205]+first[676:680],'%d%b%y%H%M')
# trip_time= timedelta(hours=int(first[1267:1269]),minutes=int(first[1270:1272]))
# datetime_arr=datetime_dep+trip_time



# print(general_infos(garde=garde,first=first),datetime_dep,datetime_arr,trip_time)
# print(firs_extraction(),route_extraction())


# ---------------------------------------------------------------------------------------------------------

# def insert_column(s):
#     final_s=s[:2]+':'+s[2:]
#     return final_s

# def retrieve_points(lst):
#     new_lst=[]
#     for elt in lst:
#          elt=insert_column(elt)
#          if elt.startswith('0'):
#               new_lst.append(elt[1:])
#          else:
#               new_lst.append(elt)
#     return new_lst