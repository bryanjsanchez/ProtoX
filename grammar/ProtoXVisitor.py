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
        # ADD functions
        if ctx.ADD():
            # add procedure procedureID to hospital hospitalID
            if ctx.PROC() and ctx.HOSP() and ctx.TEXT(0) and ctx.TEXT(1):
                addProcedureToHospital(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
            # add protocol protocolID to procedure procedureID
            elif ctx.PROTO() and ctx.PROC() and ctx.TEXT(0) and ctx.TEXT(1):
                addProtocoltoProcedure(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
            # add protocol to hospital not alloweda
            elif ctx.HOSP() and ctx.PROTO():
                print("Incorrect command.")
            # add hospital hospitalID
            elif ctx.HOSP() and ctx.TEXT(0):
                addHospital(str(ctx.TEXT(0))[1:-1])
            # add procedure procedureID
            elif ctx.PROC() and ctx.TEXT(0):
                addProcedure(str(ctx.TEXT(0))[1:-1])
            # add protocol protocolID protocolText
            elif ctx.PROTO() and ctx.TEXT(0) and ctx.TEXT(1):
                addProtocol(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
        #SHOW functions
        elif ctx.SHOW():
            # show hospital procedures
            if ctx.HOSP() and ctx.PROC() and ctx.TEXT():
                showHospitalProcedures(str(ctx.TEXT(0))[1:-1])
            # show hospital protocols
            elif ctx.HOSP() and ctx.PROTO() and ctx.TEXT():
                showHospitalProtocols(str(ctx.TEXT(0))[1:-1])
            # show procedure protocols
            elif ctx.PROC() and ctx.PROTO() and ctx.TEXT():
                showProcedureProtocols(str(ctx.TEXT(0))[1:-1])
            # show hospitals
            elif ctx.HOSP():
                showHospitals()
            # show procedures
            elif ctx.PROC():
                showProcedures()
            # show protocol protocolID
            elif ctx.PROTO() and ctx.TEXT(0):
                showProtocol(str(ctx.TEXT(0))[1:-1])
            # show protocols
            elif ctx.PROTO():
                showProtocols()
        elif ctx.DELETE():
            # delete procedure from hospital
            if ctx.PROC() and ctx.HOSP() and ctx.TEXT(0) and ctx.TEXT(1):
                deleteProcedureFromHospital(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
            # delete protocol from procedure
            elif ctx.PROC() and ctx.PROTO() and ctx.TEXT(0) and ctx.TEXT(1):
                deleteProtocolFromProcedure(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])
            # delete hospitals
            elif ctx.HOSP() and ctx.TEXT(0):
                deleteHospitals(str(ctx.TEXT(0))[1:-1])
            # delete procedures
            elif ctx.PROC() and ctx.TEXT(0):
                deleteProcedures(str(ctx.TEXT(0))[1:-1])
            # delete protocols
            elif ctx.PROTO() and ctx.TEXT(0):
                deleteProtocols(str(ctx.TEXT(0))[1:-1])
        # edit protocol
        elif ctx.EDIT():
            if ctx.PROTO() and ctx.TEXT(0) and ctx.WITH() and ctx.TEXT(1):
                editProtocol(str(ctx.TEXT(0))[1:-1], str(ctx.TEXT(1))[1:-1])


def addProcedureToHospital(procedureID, hospitalID):
    hospitals = loadHospitals()
    procedures = loadProcedures()
    if hospitalID in hospitals.keys() and procedureID in procedures.keys():
        if procedureID not in hospitals[hospitalID]:
            hospitals[hospitalID].append(procedureID)
            saveHospitals(hospitals)
            print("Procedure '%s' added to hospital '%s'." % (procedureID, hospitalID))
            return
        else:
            print("Procedure '%s' already in hospital '%s'." % (procedureID, hospitalID))
            return
    if hospitalID not in hospitals.keys():
        print("Hospital '%s' does not exist. Please create hospital." % hospitalID)
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist. Please create procedure." % procedureID)

def addProtocoltoProcedure(protocolID, procedureID):
    procedures = loadProcedures()
    protocols = loadProtocols()
    if procedureID in procedures.keys() and protocolID in protocols.keys():
        if protocolID not in procedures[procedureID]:
            procedures[procedureID].append(protocolID)
            saveProcedures(procedures)
            print("Protocol '%s' added to procedure '%s'." % (protocolID, procedureID))
            return
        else:
            print("Protocol '%s' already in procedure '%s'." % (protocolID, procedureID))
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist. Please create procedure." % procedureID)
    if protocolID not in protocols.keys():
        print("Protocol '%s' does not exist. Please create protocol." % protocolID)

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


def showHospitalProcedures(hospitalID):
    hospitals = loadHospitals()
    if hospitalID in hospitals:
        for h in hospitals[hospitalID]:
            print(h)
    else:
        print("Hospital '%s' not found." % hospitalID)

def showHospitalProtocols(hospitalID):
    hospitals = loadHospitals()
    if hospitalID in hospitals:
        procedures = loadProcedures()
        protocols = set()
        for proc in hospitals[hospitalID]:
            for proto in procedures[proc]:
                protocols.add(proto)
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
    for proto in protocols.keys():
        if proto.lower() == protocolID.lower():
            print(protocols[proto])
            return
    print("Protocol '%s' not found." % protocolID)

def deleteProcedureFromHospital(procedureID, hospitalID):
    hospitals = loadHospitals()
    procedures = loadProcedures()
    if hospitalID in hospitals.keys() and procedureID in procedures.keys():
        if procedureID in hospitals[hospitalID]:
            hospitals[hospitalID].remove(procedureID)
            saveHospitals(hospitals)
            print("Procedure '%s' deleted from hospital '%s'." % (procedureID, hospitalID))
            return
        else:
            print("Procedure '%s' not in hospital '%s'." % (procedureID, hospitalID))
            return
    if hospitalID not in hospitals.keys():
        print("Hospital '%s' does not exist." % hospitalID)
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist." % procedureID)

def deleteProtocolFromProcedure(protocolID, procedureID):
    procedures = loadProcedures()
    protocols = loadProtocols()
    if procedureID in procedures.keys() and protocolID in protocols.keys():
        if protocolID in procedures[procedureID]:
            procedures[procedureID].remove(protocolID)
            saveProcedures(procedures)
            print("Protocol '%s' deleted from procedure '%s'." % (protocolID, procedureID))
            return
        else:
            print("Protocol '%s' not in procedure '%s'." % (protocolID, procedureID))
            return
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist." % procedureID)
    if protocolID not in protocols.keys():
        print("Protocol '%s' does not exist." % protocolID)

def deleteHospitals(hospitalID):
    hospitals = loadHospitals()
    if hospitalID in hospitals.keys():
        del hospitals[hospitalID]
        saveHospitals(hospitals)
        print("Hospital '%s' deleted." % hospitalID)
    else:
        print("Hospital '%s' does not exist." % hospitalID)

def deleteProcedures(procedureID):
    procedures = loadProcedures()
    if procedureID not in procedures.keys():
        print("Procedure '%s' does not exist." % procedureID)
    else:
        hospitals = loadHospitals()
        hospitalsList = []
        for h in hospitals.keys():
            if procedureID in hospitals[h]:
                hospitalsList.append(h)
        if not hospitalsList:
            del procedures[procedureID]
            saveProcedures(procedures)
            print("Procedure '%s' deleted." % procedureID)
        else:
            print("Procedure '%s' is in use by: " % procedureID)
            for h in hospitalsList:
                print(h)

def deleteProtocols(protocolID):
    protocols = loadProtocols()
    if protocolID not in protocols.keys():
        print("Protocol '%s' does not exist." % protocolID)
    else:
        procedures = loadProcedures()
        proceduresList = []
        for proc in procedures.keys():
            if protocolID in procedures[proc]:
                proceduresList.append(proc)
        if not proceduresList:
            del protocols[protocolID]
            saveProtocols(protocols)
            print("Protocol '%s' deleted." % protocolID)
        else:
            print("Protocol '%s' is in use by: " % protocolID)
            for proc in proceduresList:
                print(proc)


def editProtocol(protocolID, text):
    protocols = loadProtocols()
    if protocolID in protocols.keys():
        protocols[protocolID] = text
        print("Edited protocol '%s'." % protocolID)
        saveProtocols(protocols)
    else:
        print("Protocol '%s' not found." % protocolID)


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