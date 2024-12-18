#!/usr/bin/env python3
import argparse
from intermine.webservice import Service

def get_properties(file_path):
    """
    Reads the properties file and retrieves the list_token.

    Args:
        file_path (str): Path to the properties file.

    Returns:
        str: The retrieved list_token.

    Raises:
        ValueError: If the list_token is not found in the properties file.
    """
    token = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('list_token'):
                token = line.split('=', 1)[1].strip()  # Strip whitespace and newline characters

    if token is None:
        raise ValueError("Token not found in properties file.")

    return token

def main():
    """
    Main function to recreate public lists in Alliance based on the provided environment flag.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Recreate public lists in Alliance.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--stage', action='store_true', help='Run in staging environment')
    group.add_argument('--prod', action='store_true', help='Run in production environment')
    args = parser.parse_args()

    # Path to the properties file
    properties_file_path = 'alliancemine.properties'

    # Get the token from the properties file
    token = get_properties(properties_file_path)

    # Determine the service URL based on the environment
    if args.stage:
        service_url = "https://stage.alliancegenome.org/alliancemine/service"
    elif args.prod:
        service_url = "https://www.alliancegenome.org/alliancemine/service"
    else:
        raise ValueError("Either --stage or --prod must be specified.")

    # Initialize the service with the appropriate URL and token
    service = Service(service_url, token=token)

    # Initialize the List Manager
    lm = service.list_manager()

    # Delete existing lists to ensure a fresh start
    lm.delete_lists([
        "Curated Macromolecular Complexes", 
        "RNA genes and rRNA spacer regions", 
        "rRNA and spacer regions", 
        "Retrotransposons", 
        "Uncharacterized_Verified_ORFs", 
        "ALL_Verified_Uncharacterized_Dubious_ORFs", 
        "Verified_ORFs", 
        "Dubious_ORFs", 
        "Uncharacterized_ORFs", 
        "Long Terminal Repeat", 
        "Telomeres", 
        "RetroTransposons", 
        "NotPhysicallyMapped", 
        "Centromeres", 
        "ARSs", 
        "tRNAs", 
        "All Curated Macromolecular Complexes", 
        "Human genes with yeast homologs", 
        "Human genes complementing or complemented by yeast genes", 
        "Not In Systematic Sequence Of S288C", 
        "snoRNAs", 
        "snRNAs", 
        "ALL_Yeast_Genes"
    ])

    ### Verified_ORF ###
    query1 = service.new_query()
    query1.add_view("Gene.primaryIdentifier")
    query1.add_constraint("Gene.qualifier", "=", "Verified")
    query1.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    verified_orf_list = service.create_list(
        query1, 
        "Gene", 
        name="Verified_ORFs", 
        description="Verified ORFs", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Dubious_ORF ###
    query2 = service.new_query()
    query2.add_view("Gene.primaryIdentifier")
    query2.add_constraint("Gene.qualifier", "=", "Dubious")
    query2.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    dubious_orf_list = service.create_list(
        query2, 
        "Gene", 
        name="Dubious_ORFs", 
        description="Dubious ORFs", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Uncharacterized_ORFs ###
    query3 = service.new_query()
    query3.add_view("Gene.primaryIdentifier")
    query3.add_constraint("Gene.qualifier", "=", "Uncharacterized")
    query3.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    uncharacterized_orf_list = service.create_list(
        query3, 
        "Gene", 
        name="Uncharacterized_ORFs", 
        description="Uncharacterized ORFs", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Uncharacterized_Verified_ORFs ###
    queryX = service.new_query()
    queryX.add_view("Gene.primaryIdentifier")
    queryX.add_constraint("qualifier", "ONE OF", ["Uncharacterized", "Verified"])
    queryX.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    unchar_ver_orf_list = service.create_list(
        queryX, 
        "Gene", 
        name="Uncharacterized_Verified_ORFs", 
        description="This List excludes Dubious ORFs", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### ALL_Verified_Uncharacterized_Dubious_ORFs ###
    queryY = service.new_query()
    queryY.add_view("Gene.primaryIdentifier")
    queryY.add_constraint("qualifier", "ONE OF", ["Uncharacterized", "Verified", "Dubious"])
    queryY.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    unchar_ver_dub_orf_list = service.create_list(
        queryY, 
        "Gene", 
        name="ALL_Verified_Uncharacterized_Dubious_ORFs", 
        description="This List includes ALL ORFs", 
        tags=["im:public", "im:frontpage"]
    )
    
    ## Telomeres ###
    query4 = service.new_query()
    query4.add_view("Telomere.primaryIdentifier")
    query4.add_constraint("Telomere.featureType", "=", "telomere")
    query4.add_constraint("Telomere.organism.shortName", "=", "S. cerevisiae")
    telomere_list = service.create_list(
        query4, 
        "Telomere", 
        name="Telomeres", 
        description="Telomeres", 
        tags=["im:public"]
    )
    
    ### RetroTransposons ###
    query5 = service.new_query()
    query5.add_view("Retrotransposon.primaryIdentifier")
    query5.add_constraint("Retrotransposon.organism.shortName", "=", "S. cerevisiae")
    retro_list = service.create_list(
        query5, 
        "Retrotransposon", 
        name="Retrotransposons", 
        description="Retrotransposons", 
        tags=["im:public"]
    )
    
    ### Centromeres ###
    query7 = service.new_query()
    query7.add_view("Centromere.primaryIdentifier")
    query7.add_constraint("Centromere.organism.shortName", "=", "S. cerevisiae")
    centromere_list = service.create_list(
        query7, 
        "Centromere", 
        name="Centromeres", 
        description="Centromeres", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### ARSs ###
    query8 = service.new_query()
    query8.add_view("ARS.primaryIdentifier")
    query8.add_constraint("ARS.organism.shortName", "=", "S. cerevisiae")
    ars_list = service.create_list(
        query8, 
        "ARS", 
        name="ARSs", 
        description="", 
        tags=["im:public"]
    )
    
    ### tRNAs ###
    query9 = service.new_query()
    query9.add_view("TRNAGene.primaryIdentifier")
    query9.add_constraint("TRNAGene.organism.shortName", "=", "S. cerevisiae")
    trna_list = service.create_list(
        query9, 
        "TRNAGene", 
        name="tRNAs", 
        description="", 
        tags=["im:public"]
    )
    
    ### snRNAs ###
    query14 = service.new_query()
    query14.add_view("SnRNAGene.primaryIdentifier")
    query14.add_constraint("SnRNAGene.organism.shortName", "=", "S. cerevisiae")
    snrna_list = service.create_list(
        query14, 
        "SnRNAGene", 
        name="snRNAs", 
        description="", 
        tags=["im:public"]
    )
    
    ### snoRNAs ###
    query15 = service.new_query()
    query15.add_view("SnoRNAGene.primaryIdentifier")
    query15.add_constraint("SnoRNAGene.organism.shortName", "=", "S. cerevisiae")
    snorna_list = service.create_list(
        query15, 
        "SnoRNAGene", 
        name="snoRNAs", 
        description="", 
        tags=["im:public"]
    )
    
    ### Not In Systematic Sequence Of S288C ###
    query16 = service.new_query()
    query16.add_view("NotInSystematicSequenceOfS288C.primaryIdentifier")
    query16.add_constraint("NotInSystematicSequenceOfS288C.organism.shortName", "=", "S. cerevisiae")
    niss_list = service.create_list(
        query16, 
        "NotInSystematicSequenceOfS288C", 
        name="Not In Systematic Sequence Of S288C", 
        description="", 
        tags=["im:public"]
    )
    
    ### rRNAs ###
    query17 = service.new_query()
    query17.add_view("RRNAGene.primaryIdentifier")
    query17.add_constraint("RRNAGene.organism.shortName", "=", "S. cerevisiae")
    rrna_list = service.create_list(
        query17, 
        "RRNAGene", 
        name="rRNA and spacer regions", 
        description="rRNA and spacer regions", 
        tags=["im:public"]
    )
    
    ### RNA genes and rRNA spacer regions ###
    queryY = service.new_query()
    queryY.add_view("Gene.primaryIdentifier")
    queryY.add_constraint("featureType", "ONE OF", [
        "tRNA gene", "snoRNA gene", "rRNA gene", "snRNA gene", "telomerase RNA gene"
    ])
    queryY.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    unchar_ver_dub_orf_list = service.create_list(
        queryY, 
        "Gene", 
        name="RNA genes and rRNA spacer regions", 
        description="", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Long Terminal Repeats ###
    query10 = service.new_query()
    query10.add_view("LongTerminalRepeat.primaryIdentifier")
    query10.add_constraint("LongTerminalRepeat.status", "=", "Active")
    query10.add_constraint("LongTerminalRepeat.organism.shortName", "=", "S. cerevisiae")
    ltr_list = service.create_list(
        query10, 
        "LongTerminalRepeat", 
        name="Long Terminal Repeat", 
        description="", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Molecular Complexes ###
    query11 = service.new_query()
    query11.add_view("Complex.identifier")
    complex_list = service.create_list(
        query11, 
        "Complex", 
        name="Curated Macromolecular Complexes", 
        description="All curated molecular complexes", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Human Genes with Orthologs ###
    query12 = service.new_query()
    query12.add_view("Gene.primaryIdentifier", "Gene.secondaryIdentifier", "Gene.symbol", "Gene.name")
    query12.add_constraint("Gene.organism.shortName", "=", "H. sapiens")
    query12.add_constraint("Gene.homologues.homologue.organism.shortName", "=", "S. cerevisiae")
    human_list = service.create_list(
        query12, 
        "Gene", 
        name="Human genes with yeast homologs", 
        description="", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### Human Genes that Complement ###
    query13 = service.new_query()
    query13.add_view("Gene.primaryIdentifier", "Gene.secondaryIdentifier", "Gene.symbol", "Gene.name")
    query13.add_constraint("Gene.organism.shortName", "=", "H. sapiens")
    query13.add_constraint("Gene.complements.complement.organism.shortName", "=", "S. cerevisiae")
    human_list = service.create_list(
        query13, 
        "Gene", 
        name="Human genes complementing or complemented by yeast genes", 
        description="", 
        tags=["im:public", "im:frontpage"]
    )
    
    ### ALL_Yeast_Genes ###
    queryAll = service.new_query()
    queryAll.add_view("Gene.primaryIdentifier")
    queryAll.add_constraint("Gene.organism.shortName", "=", "S. cerevisiae")
    queryAll.add_constraint("featureType", "ONE OF", [
        "ORF", "tRNA gene", "ncRNA gene", "rRNA gene", "snoRNA gene", 
        "snRNA gene", "pseudogene", "blocked reading frame", 
        "intein encoding region", "recombination enhancer", 
        "telomerase RNA gene", "transposable element gene", "not in systematic sequence of S288C"
    ])
    all_yeast_genes = service.create_list(
        queryAll, 
        "Gene", 
        name="ALL_Yeast_Genes", 
        description="Contains features of the following types: ORFs, tRNAs, ncRNAs, rRNAs, snoRNAs, snRNAs, pseudogenes, blocked reading frames, intein encoding regions, recombination enhancers, telomerase RNA genes, transposable element genes and those not in systematic sequence of S288C", 
        tags=["im:public", "im:frontpage"]
    )

if __name__ == "__main__":
    main()