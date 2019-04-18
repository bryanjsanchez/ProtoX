from grammar.build.ProtoXParser import ProtoXParser
from grammar.build.ProtoXVisitor import ProtoXVisitor as ProtoXVisitorOriginal
import pickle
import os


class ProtoXVisitor(ProtoXVisitorOriginal):
    def visitProg(self, ctx):
        return super(ProtoXVisitor, self).visitProg(ctx)

    def visitStatements(self, ctx):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx: ProtoXParser.ExprContext):
        # add procedure procedureID to hospital hospitalID
        if ctx.ADD() and ctx.PROC() and ctx.HOSP() and ctx.TEXT(0) and ctx.TEXT(1):
            addProcedureToHospital(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
        # add hospital hospitalID
        elif ctx.ADD() and ctx.HOSP() and ctx.TEXT(0):
            addHospital(str(ctx.TEXT(0))[1:-1])
        # add procedure procedureID
        elif ctx.ADD() and ctx.PROC() and ctx.TEXT(0):
            addProcedure(str(ctx.TEXT(0))[1:-1])
        # add protocol protocolID protocolText
        elif ctx.ADD() and ctx.PROTO() and ctx.TEXT(0) and ctx.TEXT(1):
            addProtocol(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
        # show hospital procedures
        elif ctx.SHOW() and ctx.HOSP and ctx.PROC() and ctx.TEXT():
            showHospitalProcedures(str(ctx.TEXT(0))[1:-1])
        # show hospital protocols
        elif ctx.SHOW() and ctx.HOSP() and ctx.PROTO() and ctx.TEXT():
            showHospitalProtocols(str(ctx.TEXT(0))[1:-1])
        # show procedure protocols
        elif ctx.SHOW() and ctx.PROC() and ctx.PROTO() and ctx.TEXT():
            showProcedureProtocols(str(ctx.TEXT(0))[1:-1])
        # show hospitals
        elif ctx.SHOW() and ctx.HOSP():
            showHospitals()
        # show procedures
        elif ctx.SHOW() and ctx.PROC():
            showProcedures()
        # show protocol protocolID
        elif ctx.SHOW() and ctx.PROTO() and ctx.TEXT(0):
            showProtocol(str(ctx.TEXT(0))[1:-1])
        # show protocols
        elif ctx.SHOW() and ctx.PROTO():
            showProtocols()

def showHospitalProcedures(hospitalID):
    hospitals = loadHospitals()
    if hospitalID in hospitals:
        for h in hospitals[hospitalID]:
            print(h)
    else:
        print("Hospital '%s' not found." % hospitalID)

def showHospitalProtocols(hospitalID):
    hospitals = loadHospitals()
    procedures = loadProcedures()
    if hospitalID in hospitals:
        protocols = set()
        for proc in hospitals[hospitalID]:
            protocols.add(procedures[proc])
        for proto in protocols:
            print(proto)
    else:
        print("Hospital '%s' not found." % hospitalID)

def showProcedureProtocols(procedureID):
    procedures = loadProcedures()
    if procedureID in procedures:
        for p in procedures[procedureID]:
            print(p)
    else:
        print("Procedure '%s' not found." % procedureID)
def showHospitals():
    hospitals = loadHospitals()
    if not hospitals:
        print("No hospitals on record.")
    else:
        for h in hospitals.keys():
            print(h)

def showProcedures():
    procedures = loadProcedures()
    if not procedures:
        print("No procedures on record.")
    else:
        for p in procedures.keys():
            print(p)

def showProtocols():
    protocols = loadProtocols()
    if not protocols:
        print("No protocols on record.")
    else:
        for p in protocols.keys():
            print(p)

def showProtocol(protocolID):
    protocols = loadProtocols()
    if protocolID in protocols.keys():
        print(protocols[protocolID])
    else:
        print("Protocol '%s' not found." % protocolID)

def addHospital(hospitalID):
    hospitals = loadHospitals()
    if hospitalID not in hospitals:
        hospitals[hospitalID] = []
        saveHospitals(hospitals)
        print("Added hospital '%s'" % hospitalID)
    else:
        print("Hospital '%s' already exists." % hospitalID)

def addProcedure(procedureID):
    procedures = loadProcedures()
    if procedureID not in procedures:
        procedures[procedureID] = []
        saveProcedures(procedures)
        print("Added procedure '%s'." % procedureID)
    else:
        print("Procedure '%s' already exists." % procedureID)

def addProtocol(protocolID, protocolText):
    protocols = loadProtocols()
    if protocolID not in protocols:
        protocols[protocolID] = protocolText
        saveProtocols(protocols)
        print("Added protocol '%s'." % protocolID)
    else:
        print("Protocol '%s' already exists." % protocolID)

def addProcedureToHospital(procedureID, hospitalID):
    hospitals = loadHospitals()
    procedures = loadProcedures()
    if hospitalID in hospitals.keys() and procedureID in procedures.keys():
        hospitals[hospitalID].append(procedureID)
        saveHospitals(hospitals)
        print("Procedure '%s' added to hospital '%s'." % (procedureID, hospitalID))
        return
    if hospitalID not in hospitals.keys():
        print("Hospital '%s' does not exist. Please create hospital." % hospitalID)
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist. Please create procedure." % procedureID)


def loadHospitals():
    if os.path.isfile('grammar/data/hospitals.pickle'):
        file = open('grammar/data/hospitals.pickle', 'rb')
        hospitals = pickle.load(file)
        file.close()
    else:
        hospitals = {}
    return hospitals

def loadProcedures():
    if os.path.isfile('grammar/data/procedures.pickle'):
        file = open('grammar/data/procedures.pickle', 'rb')
        procedures = pickle.load(file)
        file.close()
    else:
        procedures = {}
    return procedures

def loadProtocols():
    if os.path.isfile('grammar/data/protocols.pickle'):
        file = open('grammar/data/protocols.pickle', 'rb')
        protocols = pickle.load(file)
        file.close()
    else:
        protocols = {}
    return protocols

def saveHospitals(hospital):
    file = open('grammar/data/hospitals.pickle', 'wb+')
    pickle.dump(hospital, file)
    file.close()

def saveProcedures(procedure):
    file = open('grammar/data/procedures.pickle', 'wb+')
    pickle.dump(procedure, file)
    file.close()

def saveProtocols(protocol):
    file = open('grammar/data/protocols.pickle', 'wb+')
    pickle.dump(protocol, file)
    file.close()