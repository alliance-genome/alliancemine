<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib uri="/WEB-INF/struts-tiles.tld" prefix="tiles" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib prefix="fn"  uri="http://java.sun.com/jsp/jstl/functions" %>

<!-- footer.jsp -->

<br/>

 <div class="body" align="center" style="clear:both">

     <%-- <c:if test="${pageName != 'contact'}">
        <div id="contactFormDivButton">
          <im:vspacer height="11"/>
          <div class="contactButton">
             <a href="#" onclick="showContactForm();return false">
               <b><fmt:message key="feedback.title"/></b>
             </a>
          </div>
        </div>

     <div id="contactFormDiv" style="display:none;">
            <im:vspacer height="11"/>
              <tiles:get name="contactForm"/>
        </div>
      </c:if> --%>

	<div id="funding-footer">
	 	    <!-- <fmt:message key="funding"/> -->
 	    <p>Powered by</p>
 	    <a target="new" href="http://intermine.org" title="InterMine">
 	        <img src="images/icons/intermine-footer-logo.png" alt="InterMine logo" />
 	    </a>
 	</div>

<br/>
<div  class="body" align="center" style="clear:both">
<blockquote><font size="-2">AllianceMine is a collaboration between the Alliance of Genome Resources and the Intermine project at the
 <a href=" http://www.sysbiol.cam.ac.uk/"> Cambridge Systems Biology Centre</a> Copyright 2022. Funding provided by NIH NHGRI and NHLBI <a href="https://www.alliancegenome.org/funding"> Details here</a>.
</font></blockquote>

<blockquote><font size="-2">Copyright &#169; 2022 The Alliance of Genome Resources.
Alliance operates under the Creative Commons Attribution 4.0 International license <a href="https://creativecommons.org/licenses/by/4.0/"> (CC BY 4.0) </a>.</font></blockquote>

<br>

</div>
<!-- /footer.jsp -->
