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

<td>Genome annotation for MODs  Data loaded includes:
<ul>
<li>PrimaryIdentifier
<li>SecondaryIdentifier
<li>Symbol
<li>Name
<li>Length
<li>Brief Description
<li>Automated Description
<li>Feature type
<li>Locations
<li>Sequences - transfered from Chromosome in post-process
</ul>
</td>
<td> <a href="https://www.alliancegenome.org/" target="_new">Alliance</a></td>
</tr>

<tr><td class="leftcol">
<p> <h2>Disease</h2></p></td>
<td>disease annotations at Alliance</td>
<td><a href="https://fms.alliancegenome.org/download/DISEASE-ALLIANCE_COMBINED.tsv" target="_new">Disease at Alliance</a> </td>
</tr>

<tr><td class="leftcol">
<p> <h2>Function</h2></p></td>
<td>Gene Ontology</td>
<td><a href="https://fms.alliancegenome.org/api/datafile/by/GAF/
" target="_new">GAF at Alliance</a> </td>
</tr>

</table>

</div>
<!-- /dataCategories -->
