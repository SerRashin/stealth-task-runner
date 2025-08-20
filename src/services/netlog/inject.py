NETLOG_JS = r"""
if (!window.__netlog) {
  window.__netlog = { reqs: [] };
  (function(){
    const oldFetch = window.fetch;
    window.fetch = async function() {
      const url = arguments[0]?.toString ? arguments[0].toString() : String(arguments[0]);
      const method = (arguments[1] && arguments[1].method) || 'GET';
      let body = (arguments[1] && arguments[1].body) || null;
      try {
        const res = await oldFetch.apply(this, arguments);
        const clone = res.clone();
        let text = '';
        try { text = await clone.text(); } catch(e) {}
        window.__netlog.reqs.push({url, method, status: res.status, body, response: text, ts: Date.now()});
        return res;
      } catch(e) {
        window.__netlog.reqs.push({url, method, status: 0, body, response: String(e), ts: Date.now()});
        throw e;
      }
    };
    const OX = window.XMLHttpRequest;
    function XHR(){
      const x = new OX();
      let url='', method='GET', body=null;
      const open = x.open;
      x.open = function(m,u){ method=m; url=u; return open.apply(x, arguments); };
      const send = x.send;
      x.send = function(b){ body=b; return send.apply(x, arguments); };
      x.addEventListener('loadend', function(){
        try { window.__netlog.reqs.push({url, method, status: x.status, body: x.responseText, ts: Date.now()}); } catch(e){}
      });
      return x;
    }
    window.XMLHttpRequest = XHR;
  })();
}
return true;
"""
