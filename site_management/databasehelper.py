from link_app.pyrebase_settings import db

class Database:
    reg_nums = dict()
    data_points = dict()


    def __init__(self):
        pass

    def getData(self):
        all_vehicles = db.child('vehicleDetailsJordan').get()
        for vh in all_vehicles.each():
            Database.reg_nums[vh.val()["registration_number"]] = int(vh.val()["sim_number"])
        
        all_sims = db.child('vehicleTracking').get()
        for sim in all_sims.each():
            points = db.child('vehicleTracking').child(int(sim.key())).get()
            Database.data_points[int(sim.key())] = []
            for point in points.each():
                Database.data_points[int(sim.key())].append([point.val()["gps_longitude"], point.val()["gps_latitude"]])