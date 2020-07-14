<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="/WEB-INF/struts-html.tld" prefix="html" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib tagdir="/WEB-INF/tags" prefix="im"%>


<!-- dataCategories -->

<html:xhtml/>

<div class="body">
<im:boxarea title="Data" stylename="plainbox"><p><fmt:message key="dataCategories.intro"/></p></im:boxarea>


<table cellpadding="0" cellspacing="0" border="0" class="dbsources">
<tr>
<th>Data Category</th>
<th>Data</th>
<th>Source</th>
</tr>

<tr>
<td class="leftcol">
<h2><p>Genome</p></h2>
</td>

<td>Genome annotation for <i>Saccharomyces cerevisiae</i>.  Data loaded includes:
<ul>
<li>PrimaryIdentifier
<li>SecondaryIdentifier
<li>Symbol
<li>Name
<li>Length
<li>Description
<li>Feature type
<li>Locations
<li>Sequences
</ul>
</td>

<td> <a href="http://www.yeastgenome.org" target="_new">SGD</a></td>
</tr>


<tr>
<td rowspan="2" class="leftcol">
<h2><p>Homology</p></h2>
</td>

<td>Homologs for <i>Saccharomyces cerevisiae</i>.  Data loaded includes:
<ul>
<li>CGOB homologs
  <li>FungiDB homologs
  <li>S.pombe homologs
</ul>
</td>

 <td> <a href="http://www.candidagenome.org" target="_new">CGOB</a><br>
<a href="http://fungidb.org/fungidb" target="_new">FungiDB</a><br>
<a href="http://www.pombase.org" target="_new">Pombe</a>
</td>
</tr>

<tr>
<td> 
 Ortholog and paralog relationships between MOD organisms: Yeast, Human, Mouse, Rat, Fly, Worm, Mosquito and Zebrafish
</td>
<td> 
<a href="http://www.treefam.org/" target="_new">Treefam</a><br>
<a href = "http://www.ncbi.nlm.nih.gov/homologene">Homologene</a><br>
<a href ="http://www.pantherdb.org/">PantherDB</a><br>
<a href ="http://uswest.ensembl.org/info/docs/compara/index.html/">Ensembl Compara</a>
</td>
</tr>

<tr><td class="leftcol">
<p> <h2>Complementation</h2></p></td>
<td>Yeast Human gene functional complementation</td>
<td><a href="http://biogrid.org" target="_new">P_POD (via SGD)</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Disease</h2></p></td>
<td>Human disease gene annotations</td>
<td><a href="http://omim.org" target="_new">OMIM</a> </td>
</tr>


<tr><td class="leftcol">
<p> <h2>Proteins</h2></p></td>
<td>Protein annotations</td>
<td><a href="http://www.yeastgenome.org" target="_new">SGD</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Complexes</h2></p></td>
<td>Macromolecular Interaction Complexes</td>
<td><a href="http://www.ebi.ac.uk/intact/" target="_new">IntAct-SGD</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Function</h2></p></td>
<td>Gene Ontology and Pathways</td>
<td><a href="http://www.yeastgenome.org" target="_new">SGD</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Phenotypes</h2></p></td>
<td>Phenotypes</td>
<td><a href="http://www.yeastgenome.org" target="_new">SGD</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Interactions</h2></p></td>
<td>Physical and Genetic Interactions</td>
<td> <a href="http://www.thebiogrid.org" target="_new">BioGRID (via SGD) </a></td>
</tr> 

<tr><td class="leftcol">
<p><h2>Literature</h2></p></td>
<td> All publications in SGD </td>
<td><a href="http://www.yeastgenome.org" target="_new">SGD</a></td>
</tr>

<tr>
<td rowspan="2" class="leftcol">
<h2><p>Expression</p></h2>
</td>

<td>Microarray-based gene expression data</td>
<td> <a href="http://spell.yeastgenome.org/" target="_new"> SGD</a></td> 
</tr>

<tr>
<td> 
SGD Integrated Transcript data
</td>
<td> 
<a href="http://yeastgenome.org/help/analyze/yeastmine-help-page#output" target="_new"> SGD</a>
</td>
</tr>

<tr><td class="leftcol">
<p><h2> Regulation</h2></p></td>
<td> Transcription Factor and Target relationships</td>
<td> <a href="http://yeastgenome.org/" target="_new">SGD</a><br>
<a href="http://www.yeastract.com/" target="_new">YEASTRACT</a><br>
<a href="http://yetfasco.ccbr.utoronto.ca/" target="_new">YeTFaSCo</a><br></td>     
</tr>

</table>


</div>
<!-- /dataCategories -->
