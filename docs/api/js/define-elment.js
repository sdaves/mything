window.defineElement = function(tag, props, mount) {    
  class cls extends HTMLElement {
     connectedCallback() {
       mount(this);
     }
   }
   window.customElements.define(tag, cls, props);
}
