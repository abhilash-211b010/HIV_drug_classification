import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
from io import BytesIO
from PIL import Image
import os

st.set_page_config(layout="wide")

# heading of the contents underlying
st.markdown("<h2 style='color: #BDFCC9; text-decoration: underline;'>Visualization :</h1>", unsafe_allow_html=True)

# loading dataset
df = pd.read_csv("data/raw/HIV.csv")

# Provide the link to the website
website_link = "https://moleculenet.org/datasets-1"

# create a container to hold the database table
st.markdown("<style>h3 { color: #BDFCC9;text-decoration: underline; font-size: 25px; }</style>", unsafe_allow_html=True)
st.subheader("Dataset content:")
with st.expander("Click to view the table"):
     
     # Set the maximum height of the content area
     max_height = 200
     st.dataframe(df, height=max_height)

# Display a title on the webpage
st.subheader('Molecule Information Display :')

# User input for the index using a text box
index = st.text_input('Enter the index of the molecule (0 to 39999):')


# Function to display molecule information based on the index
def display_molecule_info(index):
    try:
        index = int(index)
        if 0 <= index < len(df):
            smiles = df.loc[index, 'smiles']  # 'smiles' is the column name for SMILES notation
        
            # Generate and display the molecular structure
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                # Add atom numbering to the molecular structure
                for atom in mol.GetAtoms():
                    atom.SetAtomMapNum(atom.GetIdx() + 1)  # Assign indices to atoms

                # Draw the molecule with atom indices
                drawer = rdMolDraw2D.MolDraw2DCairo(300, 300)
                drawer.DrawMolecule(mol)
                drawer.FinishDrawing()

                # Get the image with annotated atoms
                img = drawer.GetDrawingText()

                # Display the molecular structure with atom indices
                st.image(img, caption="Molecular structure of selected index")
                
            else:
                st.write("Unable to generate molecular structure for the given SMILES.")
        else:
            st.write("Please enter a valid index within the range.")
    except ValueError:
        st.write("Please enter a valid integer index.")


def display_charge_info(index):
    try:
        index = int(index)
        if 0 <= index < len(df):
            smiles = df.loc[index, 'smiles']  # 'smiles' is the column name for SMILES notation

            # Generate the molecule
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                # Calculate Gasteiger Charges
                AllChem.ComputeGasteigerCharges(mol)

                # Create a copy of the molecule
                mol_with_charges = Chem.Mol(mol)
                
                # Add Gasteiger Charges as atom notes
                for at in mol_with_charges.GetAtoms():
                    lbl = '%.2f' % (at.GetDoubleProp("_GasteigerCharge"))
                    at.SetProp('atomNote', lbl)

                # Display the molecule with atom notes
                img = Draw.MolToImage(mol_with_charges)

                # Display the molecular structure with charges as annotations
                st.image(img, caption="Molecule with Gasteiger Charges as annotations")
            else:
                st.write("Unable to generate molecular structure for the given SMILES.")
        else:
            st.write("Please enter a valid index within the range.")
    except ValueError:
        st.write("Please enter a valid integer index.")


# Function to display stereo annotations for a molecule based on index
def display_stereo_annotations(index):
    try:
        index = int(index)
        if 0 <= index < len(df):
            smiles = df.loc[index, 'smiles']  # 'smiles' is the column name for SMILES notation
            
            IPythonConsole.drawOptions.addAtomIndices = False
            IPythonConsole.drawOptions.addStereoAnnotation = True
            
            # Create the molecule from SMILES
            mol = Chem.MolFromSmiles(smiles)
            
            # Draw the molecule with stereo annotations
            img = Draw.MolToImage(mol, size=(250, 250))
            
            # Display the molecule with stereo annotations
            st.image(img, caption="Molecule with Stereo Annotations")
            
        else:
            st.write("Please enter a valid index within the range.")
    except ValueError:
        st.write("Please enter a valid integer index.")



def highlight_molecule(index):
    try:
        index = int(index)
        if 0 <= index < len(df):
            smiles = df.loc[index, 'smiles']  # 'smiles' is the column name for SMILES notation
            
            # Create the molecule from SMILES
            mol = Chem.MolFromSmiles(smiles)
            
            # Define the highlighting logic (atoms and bonds to highlight)
            rgba_color = (0.0, 0.0, 1.0, 0.1)  # Transparent blue
            
            atoms = [atom.GetIdx() for atom in mol.GetAtoms()]
            
            bonds = []
            for bond in mol.GetBonds():
                aid1 = atoms[bond.GetBeginAtomIdx()]
                aid2 = atoms[bond.GetEndAtomIdx()]
                bonds.append(mol.GetBondBetweenAtoms(aid1, aid2).GetIdx())
            
            # Create a drawing object
            drawer = rdMolDraw2D.MolDraw2DCairo(350, 300)
            drawer.drawOptions().fillHighlights = True
            drawer.drawOptions().setHighlightColour(rgba_color)
            drawer.drawOptions().highlightBondWidthMultiplier = 20
            drawer.drawOptions().clearBackground = False
            rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol, highlightAtoms=atoms, highlightBonds=bonds)
            
            # Get the image
            img = Image.open(BytesIO(drawer.GetDrawingText()))
            
            # Display the highlighted molecule
            st.image(img, caption="Molecule with Highlighted Atoms and Bonds")
            
        else:
            st.write("Please enter a valid index within the range.")
    except ValueError:
        st.write("Please enter a valid integer index.")

# Create columns for button alignment
col1, col2, col3, col4 = st.columns(4)

# Display buttons in a row
with col1:
    if st.button('Draw molecule', key='molecule_button', help="Click to display molecule"):
        display_molecule_info(index)

with col2:
    if st.button('Show charges', key='charge_button', help="Click to show charges"):
        display_charge_info(index)

with col3:
    if st.button('Include Stereo Annotations(if any)', key='stereo_annotations_button', help="Click to include stereo annotations"):
        display_stereo_annotations(index)

with col4:
    if st.button('Highlight Molecule', key='highlight_button', help="Click to highlight specific atoms and bonds"):
        highlight_molecule(index)


# Display the link to the website
website_link = "https://moleculenet.org/datasets-1"

styled_link = f'<a style="color: #00FA9A !important;" href="{website_link}" target="_blank">moleculenet.org</a>'
st.markdown(
    """
    <style>
    a {
        color: #00FA9A !important;
    }
    </style>
    """
    + f"<span style='color: #00FA9A;'>***Dataset Source :***</span> {styled_link}",
    unsafe_allow_html=True
)

st.markdown('<a href="http://localhost:8501/" target="_blank">Go to Home Page</a>', unsafe_allow_html=True)