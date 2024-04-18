#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:06:54 2024

@author: dduque
"""
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import streamlit as st

comentario="""

for numero_personas in range(1,19):
    
    df1=df[df["hhsize"]==str(numero_personas)]
    df1.to_csv(r"data/"+str(numero_personas)+"sub.csv")

"""
#load data
@st.cache_data
def load():
    df=pd.read_excel(r"data/intermediate_income_calulations.xlsx")
    
    df["hhsize"]=df["hhsize"].astype(str)
    df=df[df["HHincome"]<1e7]
    df=df[df["HHincome"]>1]
    #we reorder the categories
    numero_personas=[]
    for i in range(1,19):
        numero_personas.append(str(i))
    df['Personas por hogar'] = pd.Categorical(df['hhsize'],
                                              numero_personas)
    return df

st.title("Ingresos de hogares")

tab0,tab1 = st.tabs(["Tu Ingreso","todos los datos"])
with tab0:
    
    numero_personas_hogar = st.selectbox("personas en tu hogar",
       [i for i in range(1,17)])
    
    df1=pd.read_csv(r"data/"+str(numero_personas_hogar)+"sub.csv")
    ingreso = st.number_input('Inserte el ingreso de su hogar')
    
    fig, ax = plt.subplots()
    seaborn.violinplot(ax=ax, data=df1,x="HHincome",hue="hhsize")
    ax.axvline(ingreso)
    st.pyplot(fig)



    df=pd.read_excel(r"data/intermediate_income_calulations.xlsx")
    
    df["hhsize"]=df["hhsize"].astype(str)
    df=df[df["HHincome"]<1e7]
    df=df[df["HHincome"]>1]
    #we reorder the categories
    numero_personas=[]
    for i in range(1,19):
        numero_personas.append(str(i))
    df['Personas por hogar'] = pd.Categorical(df['hhsize'],
                                              numero_personas)




with tab1:
    df=load()
    #some nice graphs that we won´t use
    #a code to make subsets of data
    fig,ax=plt.subplots()
    g=seaborn.JointGrid(df,x="HHincome", y='Personas por hogar'
                     #cbar=True, 
                     #legend=True,
                     )
    #lets makes some lines
    numero_personas_hogar2 = st.selectbox("personas",
       [i for i in range(1,17)])
    ingreso2 = st.number_input('ingreso de su hogar')


    g.plot_joint(seaborn.histplot,hue_order=["1","2","3","4","5"],ax=ax)
    g.plot_marginals(seaborn.violinplot,inner="quart")
    for vx in (g.ax_joint, g.ax_marg_y):
        vx.axvline(ingreso2, color='crimson', ls='--', lw=3)
    for hx in (g.ax_joint, g.ax_marg_y):
        hx.axhline(numero_personas_hogar2, color='crimson', ls='--', lw=3)
        
    
    st.pyplot(g) 





