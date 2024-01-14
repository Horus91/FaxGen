from pypdf import PdfReader
from pathlib import Path
from datetime import datetime,timedelta

OFPS_DIR= Path(__file__).resolve().parent.parent.joinpath('media').joinpath('ofps')


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
        callsign=self.garde[14:21]
        origin=self.first[759:786]
        destination=self.first[829:856]
        alt1=self.first[899:926]
        alt2=self.first[969:996]
        return callsign,origin,destination,alt1,alt2
    
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
            
#  a=Fax_elts(fileurl=OFPS_DIR.joinpath('FlightPlan_K5461.pdf'))

# print(a.route_extraction())
            


            
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