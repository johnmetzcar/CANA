import numpy as np
import pandas as pd
from IPython.display import display
from collections import Counter
import graphviz
from copy import copy
import os
# Cana
import cana
from cana.boolean_network import BooleanNetwork
from cana.datasets.bio import BREAST_CANCER, LEUKEMIA, THALIANA
# from cana.datasets.regan_networks import pi3kcellcycleapoptosis
from cana.drawing.canalizing_map import draw_canalizing_map_graphviz
# from cana.custom_modules import visualize_schemata
# Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.text import Text
from matplotlib.patches import Circle, Rectangle, RegularPolygon
from matplotlib.collections import PatchCollection
# Networkx
import networkx as nx

class generic_canalization_analyzer():

    def __init__(self, parent = None):
        self.boolean_network = THALIANA()

    def generic_analyzer(self):
        pd.set_option('display.max_rows', 500)
        pd.options.display.float_format = '{:.2g}'.format

        node_analysis_df = pd.DataFrame({
            'node': [n.name for n in self.boolean_network.nodes],
            'k': [n.k for n in self.boolean_network.nodes],
            'k_r': [n.input_redundancy(norm=False) for n in self.boolean_network.nodes],
            'k_e': [n.effective_connectivity(norm=False) for n in self.boolean_network.nodes],
            'k_r*': [n.input_redundancy(norm=True) for n in self.boolean_network.nodes],
            'k_e*': [n.effective_connectivity(norm=True) for n in self.boolean_network.nodes],
            'k_s*': [n.input_symmetry(norm=True) for n in self.boolean_network.nodes],
        })
        # df = df[['k','k_r','k_e','k_r*','k_e*','k^{out}','k_e^{out}']]
        node_analysis_df.sort_values('k_r*', ascending=False, inplace=True)
        # display(node_analysis_df) #Not different outside of notebook ...
        print(node_analysis_df)
        # print(df.to_latex(escape=False))
        #
        drugs = [3, 4, 5, 6, 7, 8, 9]
        # dfd = node_analysis_df.loc[drugs, ['node', 'k_r*', 'k_e*', 'k_s*']]
        dfd = node_analysis_df.loc[:, ['node', 'k_r*', 'k_e*', 'k_s*']]

        print(dfd)

        node_analysis_df.loc[(node_analysis_df.k == 1), 'k_r'] = np.nan
        node_analysis_df.loc[(node_analysis_df.k == 1), 'k_e'] = np.nan
        node_analysis_df.loc[(node_analysis_df.k == 1), 'k_r*'] = np.nan
        node_analysis_df.loc[(node_analysis_df.k == 1), 'k_e*'] = np.nan
        node_analysis_df.loc[(node_analysis_df.k == 1), 'k_s*'] = np.nan
        node_analysis_df

        display(node_analysis_df.describe())

        SG = self.boolean_network.structural_graph()
        EG = self.boolean_network.effective_graph(
            threshold=-1)  # now ... what is the difference .... I have my intuition but could be very wrong. And what does -1 mean???
        #
        EG0 = self.boolean_network.effective_graph(threshold=0)
        EG0p2 = self.boolean_network.effective_graph(threshold=.2)
        EG0p4 = self.boolean_network.effective_graph(threshold=.4)
        EG0p6 = self.boolean_network.effective_graph(threshold=.6)
        EG0p8 = self.boolean_network.effective_graph(threshold=.8)

        ## This is a mess ...

        pSG = graphviz.Digraph(name='Structural Graph', engine='neato')
        pSG.attr('graph', size='10,10', concentrate='false', simplify='false', overlap='false', splines='true',
                 ratio='.7', outputorder="edgesfirst", nodesep='.25', mindist='.20')
        pSG.attr('node', pin='true', shape='box', height='0.4', fixedsize='false', margin='.05', color='black',
                 penwidth='1', fontname='Helvetica', fontcolor='black',
                 fontsize='10')  # style='filled', fillcolor='#515660',)
        pSG.attr('edge', arrowhead='normal', arrowsize='.5', penwidth='2.5')

        # for nid,SGatt in SG.nodes(data=True):
        #     label = SGatt['label']
        #     if nid in att:
        #         pos = att[nid].get('pos', '')
        #         shape = att[nid].get('shape', 'box')
        #         fillcolor = colors[att[nid].get('type')]
        #         #width = ''att[nid].get('width', '0.7')
        #         pSG.node(str(nid), label=label, pos=pos, shape=shape, fillcolor=fillcolor, )

        for nid, d in SG.nodes(data=True):
            label = d['label']
            #     ntype = att[nid].get('type')
            #     pos = att[nid].get('pos', '')
            #     shape = att[nid].get('shape')
            #     fillcolor = colors[ntype]
            pSG.node(str(nid), label=label, )  # pos=pos, shape=shape, fillcolor=fillcolor,)

        max_penwidth = 4
        for uid, vid, d in SG.edges(data=True):
            uid = str(uid)
            vid = str(vid)
            weight = '%d' % (d['weight'] * 100)
            # self loop color
            if uid == vid:
                color = '#bdbdbd'
                uid = uid + ':w'
                vid = vid + ':c'
            else:
                color = '#636363'
            pSG.edge(uid, vid, weight=weight, color=color)

        display(pSG)
        pSG.format = 'svg'
        # Export
        pSG.render("generic_graph", cleanup=True)
        pSG.render('generic_graph.gv')

        self.make_graph_vizualization_with_graphviz(graph=SG)

    def make_graph_vizualization_with_graphviz(self, graph=None, options: dict=None):
        pSG = graphviz.Digraph(name='Structural Graph', engine='neato')
        pSG.attr('graph', size='10,10', concentrate='false', simplify='false', overlap='false', splines='true',
                 ratio='.7', outputorder="edgesfirst", nodesep='.25', mindist='.20')
        pSG.attr('node', pin='true', shape='box', height='0.4', fixedsize='false', margin='.05', color='black',
                 penwidth='1', fontname='Helvetica', fontcolor='black',
                 fontsize='10')  # style='filled', fillcolor='#515660',)
        pSG.attr('edge', arrowhead='normal', arrowsize='.5', penwidth='2.5')

        # for nid,SGatt in SG.nodes(data=True):
        #     label = SGatt['label']
        #     if nid in att:
        #         pos = att[nid].get('pos', '')
        #         shape = att[nid].get('shape', 'box')
        #         fillcolor = colors[att[nid].get('type')]
        #         #width = ''att[nid].get('width', '0.7')
        #         pSG.node(str(nid), label=label, pos=pos, shape=shape, fillcolor=fillcolor, )

        for nid, d in graph.nodes(data=True):
            label = d['label']
            #     ntype = att[nid].get('type')
            #     pos = att[nid].get('pos', '')
            #     shape = att[nid].get('shape')
            #     fillcolor = colors[ntype]
            pSG.node(str(nid), label=label, )  # pos=pos, shape=shape, fillcolor=fillcolor,)

        max_penwidth = 4
        for uid, vid, d in graph.edges(data=True):
            uid = str(uid)
            vid = str(vid)
            weight = '%d' % (d['weight'] * 100)
            # self loop color
            if uid == vid:
                color = '#bdbdbd'
                uid = uid + ':w'
                vid = vid + ':c'
            else:
                color = '#636363'
            pSG.edge(uid, vid, weight=weight, color=color)

        display(pSG)
        pSG.format = 'svg'
        # Export
        pSG.render("generic_graph_from_function", cleanup=True)
        pSG.render('generic_graph_from_function.gv')

    def calculates_path_length(G, path, weight='weight'):
        path_weight_sum = 0.0
        weakest_link = np.inf
        for source, target in zip(path[:-1], path[1:]):
            edge_weight = G.edges[(source, target)][weight]
            path_weight_sum += edge_weight
            if edge_weight < weakest_link:
                weakest_link = edge_weight
        return path_weight_sum, weakest_link

    ### Are any of these in networkx?????
    ### https://networkx.org/documentation/stable/reference/functions.html?highlight=self%20loops
    def number_of_input_nodes(G):
        count = 0
        for n, d in G.nodes(data=True):
            inputs = [True if i == j else False for i, j in G.in_edges(n)]
            if inputs == [] or inputs == [True]:
                count += 1
        return count

    #
    def number_of_nodes_with_self_loop(G):
        count = 0
        for n, d in G.nodes(data=True):
            inputs = [True if i == j else False for i, j in G.in_edges(n)]
            if any(inputs):
                count += 1
        return count

    #
    def number_of_input_nodes_with_self_loop(G):
        count = 0
        for n, d in G.nodes(data=True):
            inputs = [True if i == j else False for i, j in G.in_edges(n)]
            if inputs == [True]:
                count += 1
        return count


graph_analzyer = generic_canalization_analyzer()
graph_analzyer.generic_analyzer()