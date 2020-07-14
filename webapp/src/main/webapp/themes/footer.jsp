<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib uri="/WEB-INF/struts-tiles.tld" prefix="tiles" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>

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
<blockquote><font size="-2">YeastMine is a collaboration between SGD and the Intermine project at the <a href=" http://www.sysbiol.cam.ac.uk/"> Cambridge Systems Biology Centre</a>. YeastMine is funded by NHGRI grant 2R01HG004834.
</font></blockquote>

<blockquote><font size="-2">Copyright &#169; 1997-2019 The Board of Trustees of Leland Stanford Junior University. SGD operates under the Creative Commons Attribution 4.0 International license  <a href="https://creativecommons.org/licenses/by/4.0/"> (CC BY 4.0) </a>. The SGD project at Stanford University is supported by a Genome Research Resource Grant from the US National Human Genome Research Institute, part of the US National Institutes of Health.

<br>
<br></font></blockquote>

</div>
<!-- /footer.jsp -->
