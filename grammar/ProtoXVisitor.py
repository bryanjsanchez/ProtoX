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
        if ctx.ADD() and ctx.PROC() and ctx.HOSP() and ctx.ID(0) and ctx.ID(1):
            addProcedureToHospital(ctx.ID(0), ctx.ID(1))

        elif ctx.ADD() and ctx.HOSP() and ctx.ID(0):
            addHospital(str(ctx.ID(0)))
        # ADD
        # PROC
        # ID
        # TO
        # HOSP
        # ID

def addHospital(hospitalID):
    hospitals = loadHospitals()
    if hospitalID not in hospitals:
        hospitals[hospitalID] = []
        saveHospitals(hospitals)
    else:
        print("Hospital already in List")

def addProcedureToHospital(procedureID, hospitalID):
    hospitals = loadHospitals()
    print(hospitals.keys())
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
    file = open('grammar/data/procedure.pickle', 'wb+')
    pickle.dump(procedure, file)
    file.close()

def saveProtocols(protocol):
    file = open('grammar/data/protocol.pickle', 'wb+')
    pickle.dump(protocol, file)
    file.close()