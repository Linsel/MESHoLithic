import os,sys

currentdir = os.getcwd()
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

pparentdir = os.path.dirname(parentdir)
sys.path.insert(0, pparentdir) 

from util import *


from DetermineRidges.RidgeAnalysis import LabelledMesh
from DetermineRidges.TransformLabelledMesh import TransformLabelledMesh
from Classes.Graph.GraphPlotting import ChaineOperatoire,GraphEvaluation


from IntegralInvariants.II1DClasses import MSIIChaineOperatoire


# import timing function decorator  
from Functions.EssentialDecorators import timing



# labelled meshes 
from Functions.Procedures.LabbelledMeshProcedures import ridge_prepare_procedure,kmeans_label_procedure,kmeans_slice_procedure,label_slice_procedure,export_ridges_mesh_procedure,direct_graph_area_procedure,update_label_procedure
from Functions.Procedures.SubmeshesProcedures import submeshes_procedure, submeshes_properties_procedure


from Functions.Procedures.TransformLabbelledMeshProcedures import scar_to_ridge_labels_binary_procedure,scar_to_ridge_labels_CC_procedure,ridge_CC_to_scar_labels_procedure,ridge_color_to_scar_labels_procedure

# Graph procedures
from Functions.Procedures.MSIIChaineOperatoireProcedures import CO_prepare_procedure,MSII_procedure,MSII_feature_vector_procedure,CO_concavity_procedure
from Functions.Procedures.GraphEvaluationProcedures import undirected_graph_procedure,graph_evaluation_procedure,graph_direct_parameter_procedure,direct_graph_procedure
from Functions.Procedures.ChaineOperatoireProcedures import edge_to_arrow_procedure

# minions
from minions.GigaMeshMinions import command_line_GigaMesh
from minions.MeshMinions import update_vertex_quality,update_vertex_label

#________________________
# labbeldMesh procedures

@timing
def labelledmesh_procedures (obj:LabelledMesh = None,
                             **kwargs):
   
    method = kwargs['method']
    # if obj == None:
    #     obj = LabelledMesh()

    procedures = {'ridge_prepare':ridge_prepare_procedure,
                  'kmeans_label':kmeans_label_procedure,
                  'kmeans_sclice':kmeans_slice_procedure, 
                  'label_slice':label_slice_procedure,
                  'direct_graph_area':direct_graph_area_procedure,
                  'export_ridges_mesh':export_ridges_mesh_procedure,
                  'submeshes':submeshes_procedure,
                  'submeshes_properties':submeshes_properties_procedure,
                  'update_label':update_label_procedure}

    func = procedures.get(method)

    func(obj,**kwargs)

    return obj

@timing
def transform_labelledmesh_procedures (obj:TransformLabelledMesh = None,
                                       **kwargs):

    # if obj == None:
    #     obj = TransformLabelledMesh()
    method = kwargs['method']

    procedures = {'scar_to_ridge_labels_binary':scar_to_ridge_labels_binary_procedure,
                  'scar_to_ridge_labels_CC':scar_to_ridge_labels_CC_procedure,
                  'ridge_CC_to_scar_labels':ridge_CC_to_scar_labels_procedure,
                  'ridge_color_to_scar_labels':ridge_color_to_scar_labels_procedure}

    func = procedures.get(method)

    func(obj,**kwargs)

    return obj

#____________________________
# MSII based procedures

@timing
def MSII_chaineoperatoire_procedures (obj:MSIIChaineOperatoire = None,
                                      **kwargs):
    
    method = kwargs['method']
    # obj = MSIIChaineOperatoire()

    procedures = {'CO_prepare':CO_prepare_procedure,
                  'MSII':MSII_procedure,
                  'MSII_feature_vector':MSII_feature_vector_procedure,
                  'CO_concavity':CO_concavity_procedure}

    func = procedures.get(method)

    func(obj,**kwargs)

    return obj

#____________________________
# Evaluation

@timing
def graph_procedures (  obj:GraphEvaluation = None,
                        **kwargs):
    
    method = kwargs['method']

    # obj = GraphEvaluation ()

    procedures = {'undirected_graph':undirected_graph_procedure,
                  'graph_evaluation':graph_evaluation_procedure,
                  'graph_direct_parameter':graph_direct_parameter_procedure,
                  'direct_graph':direct_graph_procedure}

    func = procedures.get(method)

    func(obj,**kwargs)

    return obj    

@timing
def co_procedures (obj:ChaineOperatoire = None,
                   **kwargs):

    method = kwargs['method']
    # obj = ChaineOperatoire ()

    procedures = {'edge_to_arrow':edge_to_arrow_procedure}

    func = procedures.get(method)

    func(obj,**kwargs)

    return obj        

# def GigaMesh_procedures (obj: object = None, 
#                            **kwargs):
    

#     # obj = ChaineOperatoire ()

#     command_line_GigaMesh(**kwargs)

#     return obj   



@timing
def procedures (obj: object = None, 
                **kwargs):
    
    class_type = kwargs['class']
    

    objects = { 'labelledmesh':LabelledMesh,
                'transform_labelledmesh':TransformLabelledMesh,
                'CO-MSII':MSIIChaineOperatoire,
                'polylinegraph':GraphEvaluation,
                'CO':ChaineOperatoire,
                'GigaMesh':object}

    if obj == None:
        obj_func = objects.get(class_type)
        obj = obj_func ()
        
    procedures = {'labelledmesh':labelledmesh_procedures,
                  'transform_labelledmesh':transform_labelledmesh_procedures,
                  'CO-MSII':MSII_chaineoperatoire_procedures,
                  'graph':graph_procedures,
                  'CO':co_procedures,
                  'GigaMesh':command_line_GigaMesh}

    func = procedures.get(class_type)

    func(obj,**kwargs)

    del obj         