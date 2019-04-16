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
            addProcedureToHospital(ctx.TEXT(0), ctx.TEXT(1))
        # add hospital hospitalID
        elif ctx.ADD() and ctx.HOSP() and ctx.TEXT(0):
            addHospital(str(ctx.TEXT(0)))
        # add procedure procedureID
        elif ctx.ADD() and ctx.PROC() and ctx.TEXT(0):
            addProcedure(str(ctx.TEXT(0)))
        # add protocol protocolID protocolText
        elif ctx.ADD() and ctx.PROTO() and ctx.TEXT(0) and ctx.TEXT(1):
            addProtocol(str(ctx.TEXT(0)), str(ctx.TEXT(1)))
        # show hospitals
        elif ctx.SHOW() and ctx.HOSP():
            showHospitals()
        # show procedures
        elif ctx.SHOW() and ctx.PROC():
            showProcedures()
        # show protocol protocolID
        elif ctx.SHOW() and ctx.PROTO() and ctx.TEXT(0):
            showProtocol(str(ctx.TEXT(0)))
        # show protocols
        elif ctx.SHOW() and ctx.PROTO():
            showProtocols()

def showHospitals():
    hospitals = loadHospitals()
    for h in hospitals.keys():
        print(h)

def showProcedures():
    procedures = loadProcedures()
    for p in procedures.keys():
        print(p)

def showProtocols():
    protocols = loadProtocols()
    for p in protocols.keys():
        print(p)

def showProtocol(protocolID):
    protocols = loadProtocols()
    if protocolID in protocols.keys():
        print(protocols[protocolID])
    else:
        print("Protocol ID not found.")

def addHospital(hospitalID):
    hospitals = loadHospitals()
    if hospitalID not in hospitals:
        hospitals[hospitalID] = []
        saveHospitals(hospitals)
    else:
        print("Hospital already in List")

def addProcedure(procedureID):
    procedures = loadProcedures()
    if procedureID not in procedures:
        procedures[procedureID] = []
        saveProcedures(procedures)
    else:
        print("Procedure already in List")

def addProtocol(protocolID, protocolText):
    protocols = loadProtocols()
    if protocolID not in protocols:
        protocols[protocolID] = protocolText
        saveProtocols(protocols)
    else:
        print("Protocol already in List")

def addProcedureToHospital(procedureID, hospitalID):
    hospitals = loadHospitals()
    procedures = loadProcedures()
    if hospitalID in hospitals.keys() and procedureID in procedures.keys():
        hospitals[hospitalID].append(procedureID)
        saveHospitals()
        return
    if hospitalID not in hospitals.keys():
        print("Hospital not in list. Please create hospital.")
    if procedureID not in procedures.keys():
        print("Procedure not in list. Please create procedure.")


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