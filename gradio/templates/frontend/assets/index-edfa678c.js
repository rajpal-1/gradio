import{S as M,i as T,s as j,G as b,e as N,H as y,C as u,g as v,m as R,E as h,p as B,t as I,q as k,n as A,N as G,I as S,K as q,B as z,M as D,L,ab as ue,b as O,f as re,l as oe,o as se,c as U,h as _e,j as ge,x as he}from"./index-ad5e9ffd.js";import"./Button-d7d8a540.js";import{B as E}from"./BlockTitle-11df09b3.js";import"./Info-f5726450.js";const w=i=>{var e=null;return i<0?e=[52,152,219]:e=[231,76,60],de(me(Math.abs(i),[255,255,255],e))},me=(i,e,t)=>{i>1&&(i=1),i=Math.sqrt(i);var n=[0,0,0],o;for(o=0;o<3;o++)n[o]=Math.round(e[o]*(1-i)+t[o]*i);return n},de=i=>"rgb("+i[0]+", "+i[1]+", "+i[2]+")",x=(i,e,t,n,o)=>{var s=n/o,r=e/t,l=0,c=0,f=i?s>r:s<r;return f?(l=e,c=l/s):(c=t,l=c*s),{width:l,height:c,x:(e-l)/2,y:(t-c)/2}};function J(i,e,t){const n=i.slice();return n[2]=e[t],n}function be(i){let e;return{c(){e=S(i[1])},m(t,n){v(t,e,n)},p(t,n){n&2&&q(e,t[1])},d(t){t&&k(e)}}}function P(i){let e,t=i[2][0]+"",n,o,s;return{c(){e=b("div"),n=S(t),o=y(),u(e,"class","item svelte-x6nxfm"),u(e,"style",s="background-color: "+w(i[2][1]))},m(r,l){v(r,e,l),h(e,n),h(e,o)},p(r,l){l&1&&t!==(t=r[2][0]+"")&&q(n,t),l&1&&s!==(s="background-color: "+w(r[2][1]))&&u(e,"style",s)},d(r){r&&k(e)}}}function ve(i){let e,t,n,o,s;t=new E({props:{$$slots:{default:[be]},$$scope:{ctx:i}}});let r=i[0],l=[];for(let c=0;c<r.length;c+=1)l[c]=P(J(i,r,c));return{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("div");for(let c=0;c<l.length;c+=1)l[c].c();u(o,"class","range svelte-x6nxfm"),u(e,"class","input-number svelte-x6nxfm")},m(c,f){v(c,e,f),R(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a]&&l[a].m(o,null);s=!0},p(c,[f]){const a={};if(f&34&&(a.$$scope={dirty:f,ctx:c}),t.$set(a),f&1){r=c[0];let _;for(_=0;_<r.length;_+=1){const g=J(c,r,_);l[_]?l[_].p(g,f):(l[_]=P(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=r.length}},i(c){s||(B(t.$$.fragment,c),s=!0)},o(c){I(t.$$.fragment,c),s=!1},d(c){c&&k(e),A(t),G(l,c)}}}function ke(i,e,t){let{interpretation:n}=e,{label:o=""}=e;return i.$$set=s=>{"interpretation"in s&&t(0,n=s.interpretation),"label"in s&&t(1,o=s.label)},[n,o]}class pe extends M{constructor(e){super(),T(this,e,ke,ve,j,{interpretation:0,label:1})}}function Q(i,e,t){const n=i.slice();return n[3]=e[t],n[5]=t,n}function we(i){let e;return{c(){e=S(i[2])},m(t,n){v(t,e,n)},p(t,n){n&4&&q(e,t[2])},d(t){t&&k(e)}}}function V(i){let e,t=i[3]+"",n,o,s;return{c(){e=b("li"),n=S(t),o=y(),u(e,"class","dropdown-item svelte-1cqwepf"),u(e,"style",s="background-color: "+w(i[0][i[5]]))},m(r,l){v(r,e,l),h(e,n),h(e,o)},p(r,l){l&2&&t!==(t=r[3]+"")&&q(n,t),l&1&&s!==(s="background-color: "+w(r[0][r[5]]))&&u(e,"style",s)},d(r){r&&k(e)}}}function ye(i){let e,t,n,o,s;t=new E({props:{$$slots:{default:[we]},$$scope:{ctx:i}}});let r=i[1],l=[];for(let c=0;c<r.length;c+=1)l[c]=V(Q(i,r,c));return{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("ul");for(let c=0;c<l.length;c+=1)l[c].c();u(o,"class","dropdown-menu svelte-1cqwepf")},m(c,f){v(c,e,f),R(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a]&&l[a].m(o,null);s=!0},p(c,[f]){const a={};if(f&68&&(a.$$scope={dirty:f,ctx:c}),t.$set(a),f&3){r=c[1];let _;for(_=0;_<r.length;_+=1){const g=Q(c,r,_);l[_]?l[_].p(g,f):(l[_]=V(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=r.length}},i(c){s||(B(t.$$.fragment,c),s=!0)},o(c){I(t.$$.fragment,c),s=!1},d(c){c&&k(e),A(t),G(l,c)}}}function Ce(i,e,t){let{interpretation:n}=e,{choices:o}=e,{label:s=""}=e;return i.$$set=r=>{"interpretation"in r&&t(0,n=r.interpretation),"choices"in r&&t(1,o=r.choices),"label"in r&&t(2,s=r.label)},[n,o,s]}class Se extends M{constructor(e){super(),T(this,e,Ce,ye,j,{interpretation:0,choices:1,label:2})}}function qe(i){let e;return{c(){e=S(i[0])},m(t,n){v(t,e,n)},p(t,n){n&1&&q(e,t[0])},d(t){t&&k(e)}}}function Be(i){let e,t,n,o,s,r,l,c,f,a,_,g,m;return t=new E({props:{$$slots:{default:[qe]},$$scope:{ctx:i}}}),{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("button"),s=b("div"),l=y(),c=b("div"),f=z("svg"),a=z("line"),_=z("line"),u(s,"class","checkbox svelte-1nw19ca"),u(s,"style",r="background-color: "+w(i[2][0])),u(a,"x1","-7.5"),u(a,"y1","0"),u(a,"x2","-2.5"),u(a,"y2","5"),u(a,"stroke","black"),u(a,"stroke-width","4"),u(a,"stroke-linecap","round"),u(_,"x1","-2.5"),u(_,"y1","5"),u(_,"x2","7.5"),u(_,"y2","-7.5"),u(_,"stroke","black"),u(_,"stroke-width","4"),u(_,"stroke-linecap","round"),u(f,"viewBox","-10 -10 20 20"),u(f,"class","svelte-1nw19ca"),u(c,"class","checkbox svelte-1nw19ca"),u(c,"style",g="background-color: "+w(i[2][1])),u(o,"class","checkbox-item svelte-1nw19ca"),D(o,"selected",i[1]),u(e,"class","input-checkbox svelte-1nw19ca")},m(d,p){v(d,e,p),R(t,e,null),h(e,n),h(e,o),h(o,s),h(o,l),h(o,c),h(c,f),h(f,a),h(f,_),m=!0},p(d,[p]){const C={};p&9&&(C.$$scope={dirty:p,ctx:d}),t.$set(C),(!m||p&4&&r!==(r="background-color: "+w(d[2][0])))&&u(s,"style",r),(!m||p&4&&g!==(g="background-color: "+w(d[2][1])))&&u(c,"style",g),(!m||p&2)&&D(o,"selected",d[1])},i(d){m||(B(t.$$.fragment,d),m=!0)},o(d){I(t.$$.fragment,d),m=!1},d(d){d&&k(e),A(t)}}}function Ie(i,e,t){let{label:n=""}=e,{original:o}=e,{interpretation:s}=e;return i.$$set=r=>{"label"in r&&t(0,n=r.label),"original"in r&&t(1,o=r.original),"interpretation"in r&&t(2,s=r.interpretation)},[n,o,s]}class Ne extends M{constructor(e){super(),T(this,e,Ie,Be,j,{label:0,original:1,interpretation:2})}}function W(i,e,t){const n=i.slice();return n[4]=e[t],n[6]=t,n}function Re(i){let e;return{c(){e=S(i[3])},m(t,n){v(t,e,n)},p(t,n){n&8&&q(e,t[3])},d(t){t&&k(e)}}}function X(i){let e,t,n,o,s,r,l,c,f,a,_=i[4]+"",g,m;return{c(){e=b("button"),t=b("div"),o=y(),s=b("div"),r=z("svg"),l=z("line"),c=z("line"),a=y(),g=S(_),m=y(),u(t,"class","checkbox svelte-1cbhr6k"),u(t,"style",n="background-color: "+w(i[1][i[6]][0])),u(l,"x1","-7.5"),u(l,"y1","0"),u(l,"x2","-2.5"),u(l,"y2","5"),u(l,"stroke","black"),u(l,"stroke-width","4"),u(l,"stroke-linecap","round"),u(c,"x1","-2.5"),u(c,"y1","5"),u(c,"x2","7.5"),u(c,"y2","-7.5"),u(c,"stroke","black"),u(c,"stroke-width","4"),u(c,"stroke-linecap","round"),u(r,"viewBox","-10 -10 20 20"),u(r,"class","svelte-1cbhr6k"),u(s,"class","checkbox svelte-1cbhr6k"),u(s,"style",f="background-color: "+w(i[1][i[6]][1])),u(e,"class","checkbox-item svelte-1cbhr6k"),D(e,"selected",i[0].includes(i[4]))},m(d,p){v(d,e,p),h(e,t),h(e,o),h(e,s),h(s,r),h(r,l),h(r,c),h(e,a),h(e,g),h(e,m)},p(d,p){p&2&&n!==(n="background-color: "+w(d[1][d[6]][0]))&&u(t,"style",n),p&2&&f!==(f="background-color: "+w(d[1][d[6]][1]))&&u(s,"style",f),p&4&&_!==(_=d[4]+"")&&q(g,_),p&5&&D(e,"selected",d[0].includes(d[4]))},d(d){d&&k(e)}}}function Ae(i){let e,t,n,o;t=new E({props:{$$slots:{default:[Re]},$$scope:{ctx:i}}});let s=i[2],r=[];for(let l=0;l<s.length;l+=1)r[l]=X(W(i,s,l));return{c(){e=b("div"),N(t.$$.fragment),n=y();for(let l=0;l<r.length;l+=1)r[l].c();u(e,"class","input-checkbox-group svelte-1cbhr6k")},m(l,c){v(l,e,c),R(t,e,null),h(e,n);for(let f=0;f<r.length;f+=1)r[f]&&r[f].m(e,null);o=!0},p(l,[c]){const f={};if(c&136&&(f.$$scope={dirty:c,ctx:l}),t.$set(f),c&7){s=l[2];let a;for(a=0;a<s.length;a+=1){const _=W(l,s,a);r[a]?r[a].p(_,c):(r[a]=X(_),r[a].c(),r[a].m(e,null))}for(;a<r.length;a+=1)r[a].d(1);r.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){I(t.$$.fragment,l),o=!1},d(l){l&&k(e),A(t),G(r,l)}}}function Me(i,e,t){let{original:n}=e,{interpretation:o}=e,{choices:s}=e,{label:r=""}=e;return i.$$set=l=>{"original"in l&&t(0,n=l.original),"interpretation"in l&&t(1,o=l.interpretation),"choices"in l&&t(2,s=l.choices),"label"in l&&t(3,r=l.label)},[n,o,s,r]}class Te extends M{constructor(e){super(),T(this,e,Me,Ae,j,{original:0,interpretation:1,choices:2,label:3})}}function Y(i,e,t){const n=i.slice();return n[6]=e[t],n}function je(i){let e;return{c(){e=S(i[5])},m(t,n){v(t,e,n)},p(t,n){n&32&&q(e,t[5])},d(t){t&&k(e)}}}function Z(i){let e,t;return{c(){e=b("div"),u(e,"style",t="background-color: "+w(i[6])),u(e,"class","svelte-1sxprr7")},m(n,o){v(n,e,o)},p(n,o){o&2&&t!==(t="background-color: "+w(n[6]))&&u(e,"style",t)},d(n){n&&k(e)}}}function Ee(i){let e,t,n,o,s,r,l,c,f,a;t=new E({props:{$$slots:{default:[je]},$$scope:{ctx:i}}});let _=i[1],g=[];for(let m=0;m<_.length;m+=1)g[m]=Z(Y(i,_,m));return{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("input"),s=y(),r=b("div");for(let m=0;m<g.length;m+=1)g[m].c();l=y(),c=b("div"),f=S(i[0]),u(o,"type","range"),o.disabled=!0,u(o,"min",i[2]),u(o,"max",i[3]),u(o,"step",i[4]),u(o,"class","svelte-1sxprr7"),u(r,"class","range svelte-1sxprr7"),u(c,"class","original svelte-1sxprr7"),u(e,"class","input-slider svelte-1sxprr7")},m(m,d){v(m,e,d),R(t,e,null),h(e,n),h(e,o),h(e,s),h(e,r);for(let p=0;p<g.length;p+=1)g[p]&&g[p].m(r,null);h(e,l),h(e,c),h(c,f),a=!0},p(m,[d]){const p={};if(d&544&&(p.$$scope={dirty:d,ctx:m}),t.$set(p),(!a||d&4)&&u(o,"min",m[2]),(!a||d&8)&&u(o,"max",m[3]),(!a||d&16)&&u(o,"step",m[4]),d&2){_=m[1];let C;for(C=0;C<_.length;C+=1){const F=Y(m,_,C);g[C]?g[C].p(F,d):(g[C]=Z(F),g[C].c(),g[C].m(r,null))}for(;C<g.length;C+=1)g[C].d(1);g.length=_.length}(!a||d&1)&&q(f,m[0])},i(m){a||(B(t.$$.fragment,m),a=!0)},o(m){I(t.$$.fragment,m),a=!1},d(m){m&&k(e),A(t),G(g,m)}}}function Ge(i,e,t){let{original:n}=e,{interpretation:o}=e,{minimum:s}=e,{maximum:r}=e,{step:l}=e,{label:c=""}=e;return i.$$set=f=>{"original"in f&&t(0,n=f.original),"interpretation"in f&&t(1,o=f.interpretation),"minimum"in f&&t(2,s=f.minimum),"maximum"in f&&t(3,r=f.maximum),"step"in f&&t(4,l=f.step),"label"in f&&t(5,c=f.label)},[n,o,s,r,l,c]}class ze extends M{constructor(e){super(),T(this,e,Ge,Ee,j,{original:0,interpretation:1,minimum:2,maximum:3,step:4,label:5})}}function $(i,e,t){const n=i.slice();return n[4]=e[t],n[6]=t,n}function De(i){let e;return{c(){e=S(i[3])},m(t,n){v(t,e,n)},p(t,n){n&8&&q(e,t[3])},d(t){t&&k(e)}}}function ee(i){let e,t,n,o,s=i[4]+"",r,l;return{c(){e=b("button"),t=b("div"),o=y(),r=S(s),l=y(),u(t,"class","radio-circle svelte-1nekfre"),u(t,"style",n="background-color: "+w(i[1][i[6]])),u(e,"class","radio-item svelte-1nekfre"),D(e,"selected",i[0]===i[4])},m(c,f){v(c,e,f),h(e,t),h(e,o),h(e,r),h(e,l)},p(c,f){f&2&&n!==(n="background-color: "+w(c[1][c[6]]))&&u(t,"style",n),f&4&&s!==(s=c[4]+"")&&q(r,s),f&5&&D(e,"selected",c[0]===c[4])},d(c){c&&k(e)}}}function Fe(i){let e,t,n,o;t=new E({props:{$$slots:{default:[De]},$$scope:{ctx:i}}});let s=i[2],r=[];for(let l=0;l<s.length;l+=1)r[l]=ee($(i,s,l));return{c(){e=b("div"),N(t.$$.fragment),n=y();for(let l=0;l<r.length;l+=1)r[l].c();u(e,"class","input-radio svelte-1nekfre")},m(l,c){v(l,e,c),R(t,e,null),h(e,n);for(let f=0;f<r.length;f+=1)r[f]&&r[f].m(e,null);o=!0},p(l,[c]){const f={};if(c&136&&(f.$$scope={dirty:c,ctx:l}),t.$set(f),c&7){s=l[2];let a;for(a=0;a<s.length;a+=1){const _=$(l,s,a);r[a]?r[a].p(_,c):(r[a]=ee(_),r[a].c(),r[a].m(e,null))}for(;a<r.length;a+=1)r[a].d(1);r.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){I(t.$$.fragment,l),o=!1},d(l){l&&k(e),A(t),G(r,l)}}}function He(i,e,t){let{original:n}=e,{interpretation:o}=e,{choices:s}=e,{label:r=""}=e;return i.$$set=l=>{"original"in l&&t(0,n=l.original),"interpretation"in l&&t(1,o=l.interpretation),"choices"in l&&t(2,s=l.choices),"label"in l&&t(3,r=l.label)},[n,o,s,r]}class Ke extends M{constructor(e){super(),T(this,e,He,Fe,j,{original:0,interpretation:1,choices:2,label:3})}}function Le(i){let e;return{c(){e=S(i[1])},m(t,n){v(t,e,n)},p(t,n){n&2&&q(e,t[1])},d(t){t&&k(e)}}}function Oe(i){let e,t,n,o,s,r,l,c,f,a;return t=new E({props:{$$slots:{default:[Le]},$$scope:{ctx:i}}}),{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("div"),s=b("div"),r=b("canvas"),l=y(),c=b("img"),u(s,"class","interpretation svelte-h0dntu"),L(c.src,f=i[0])||u(c,"src",f),u(c,"class","svelte-h0dntu"),u(o,"class","image-preview svelte-h0dntu"),u(e,"class","input-image")},m(_,g){v(_,e,g),R(t,e,null),h(e,n),h(e,o),h(o,s),h(s,r),i[6](r),h(o,l),h(o,c),i[7](c),a=!0},p(_,[g]){const m={};g&514&&(m.$$scope={dirty:g,ctx:_}),t.$set(m),(!a||g&1&&!L(c.src,f=_[0]))&&u(c,"src",f)},i(_){a||(B(t.$$.fragment,_),a=!0)},o(_){I(t.$$.fragment,_),a=!1},d(_){_&&k(e),A(t),i[6](null),i[7](null)}}}function Ue(i,e,t){let{original:n}=e,{interpretation:o}=e,{shape:s}=e,{label:r=""}=e,l,c;const f=(g,m,d,p)=>{var C=d/g[0].length,F=p/g.length,H=0;g.forEach(function(ae){var K=0;ae.forEach(function(fe){m.fillStyle=w(fe),m.fillRect(K*C,H*F,C,F),K++}),H++})};ue(()=>{let g=x(!0,c.width,c.height,c.naturalWidth,c.naturalHeight);s&&(g=x(!0,g.width,g.height,s[0],s[1]));let m=g.width,d=g.height;l.setAttribute("height",`${d}`),l.setAttribute("width",`${m}`),f(o,l.getContext("2d"),m,d)});function a(g){O[g?"unshift":"push"](()=>{l=g,t(2,l)})}function _(g){O[g?"unshift":"push"](()=>{c=g,t(3,c)})}return i.$$set=g=>{"original"in g&&t(0,n=g.original),"interpretation"in g&&t(4,o=g.interpretation),"shape"in g&&t(5,s=g.shape),"label"in g&&t(1,r=g.label)},[n,r,l,c,o,s,a,_]}class xe extends M{constructor(e){super(),T(this,e,Ue,Oe,j,{original:0,interpretation:4,shape:5,label:1})}}function te(i,e,t){const n=i.slice();return n[2]=e[t],n}function Je(i){let e;return{c(){e=S(i[1])},m(t,n){v(t,e,n)},p(t,n){n&2&&q(e,t[1])},d(t){t&&k(e)}}}function le(i){let e,t;return{c(){e=b("div"),u(e,"class","item svelte-13lmfcp"),u(e,"style",t="background-color: "+w(i[2]))},m(n,o){v(n,e,o)},p(n,o){o&1&&t!==(t="background-color: "+w(n[2]))&&u(e,"style",t)},d(n){n&&k(e)}}}function Pe(i){let e,t,n,o,s;t=new E({props:{$$slots:{default:[Je]},$$scope:{ctx:i}}});let r=i[0],l=[];for(let c=0;c<r.length;c+=1)l[c]=le(te(i,r,c));return{c(){e=b("div"),N(t.$$.fragment),n=y(),o=b("div");for(let c=0;c<l.length;c+=1)l[c].c();u(o,"class","range svelte-13lmfcp")},m(c,f){v(c,e,f),R(t,e,null),h(e,n),h(e,o);for(let a=0;a<l.length;a+=1)l[a]&&l[a].m(o,null);s=!0},p(c,[f]){const a={};if(f&34&&(a.$$scope={dirty:f,ctx:c}),t.$set(a),f&1){r=c[0];let _;for(_=0;_<r.length;_+=1){const g=te(c,r,_);l[_]?l[_].p(g,f):(l[_]=le(g),l[_].c(),l[_].m(o,null))}for(;_<l.length;_+=1)l[_].d(1);l.length=r.length}},i(c){s||(B(t.$$.fragment,c),s=!0)},o(c){I(t.$$.fragment,c),s=!1},d(c){c&&k(e),A(t),G(l,c)}}}function Qe(i,e,t){let{interpretation:n}=e,{label:o=""}=e;return i.$$set=s=>{"interpretation"in s&&t(0,n=s.interpretation),"label"in s&&t(1,o=s.label)},[n,o]}class Ve extends M{constructor(e){super(),T(this,e,Qe,Pe,j,{interpretation:0,label:1})}}function ne(i,e,t){const n=i.slice();return n[2]=e[t][0],n[3]=e[t][1],n}function We(i){let e;return{c(){e=S(i[0])},m(t,n){v(t,e,n)},p(t,n){n&1&&q(e,t[0])},d(t){t&&k(e)}}}function ie(i){let e,t=i[2]+"",n,o,s;return{c(){e=b("span"),n=S(t),o=y(),u(e,"class","text-span svelte-15c0u2m"),u(e,"style",s="background-color: "+w(i[3]))},m(r,l){v(r,e,l),h(e,n),h(e,o)},p(r,l){l&2&&t!==(t=r[2]+"")&&q(n,t),l&2&&s!==(s="background-color: "+w(r[3]))&&u(e,"style",s)},d(r){r&&k(e)}}}function Xe(i){let e,t,n,o;t=new E({props:{$$slots:{default:[We]},$$scope:{ctx:i}}});let s=i[1],r=[];for(let l=0;l<s.length;l+=1)r[l]=ie(ne(i,s,l));return{c(){e=b("div"),N(t.$$.fragment),n=y();for(let l=0;l<r.length;l+=1)r[l].c();u(e,"class","input-text svelte-15c0u2m")},m(l,c){v(l,e,c),R(t,e,null),h(e,n);for(let f=0;f<r.length;f+=1)r[f]&&r[f].m(e,null);o=!0},p(l,[c]){const f={};if(c&65&&(f.$$scope={dirty:c,ctx:l}),t.$set(f),c&2){s=l[1];let a;for(a=0;a<s.length;a+=1){const _=ne(l,s,a);r[a]?r[a].p(_,c):(r[a]=ie(_),r[a].c(),r[a].m(e,null))}for(;a<r.length;a+=1)r[a].d(1);r.length=s.length}},i(l){o||(B(t.$$.fragment,l),o=!0)},o(l){I(t.$$.fragment,l),o=!1},d(l){l&&k(e),A(t),G(r,l)}}}function Ye(i,e,t){let{label:n=""}=e,{interpretation:o}=e;return i.$$set=s=>{"label"in s&&t(0,n=s.label),"interpretation"in s&&t(1,o=s.interpretation)},[n,o]}class Ze extends M{constructor(e){super(),T(this,e,Ye,Xe,j,{label:0,interpretation:1})}}const $e={audio:Ve,dropdown:Se,checkbox:Ne,checkboxgroup:Te,number:pe,slider:ze,radio:Ke,image:xe,textbox:Ze};function ce(i){let e,t,n;const o=[i[0],{original:i[1].original},{interpretation:i[1].interpretation}];var s=i[2];function r(l){let c={};for(let f=0;f<o.length;f+=1)c=he(c,o[f]);return{props:c}}return s&&(e=U(s,r())),{c(){e&&N(e.$$.fragment),t=re()},m(l,c){e&&R(e,l,c),v(l,t,c),n=!0},p(l,c){const f=c&3?_e(o,[c&1&&ge(l[0]),c&2&&{original:l[1].original},c&2&&{interpretation:l[1].interpretation}]):{};if(c&4&&s!==(s=l[2])){if(e){oe();const a=e;I(a.$$.fragment,1,0,()=>{A(a,1)}),se()}s?(e=U(s,r()),N(e.$$.fragment),B(e.$$.fragment,1),R(e,t.parentNode,t)):e=null}else s&&e.$set(f)},i(l){n||(e&&B(e.$$.fragment,l),n=!0)},o(l){e&&I(e.$$.fragment,l),n=!1},d(l){l&&k(t),e&&A(e,l)}}}function et(i){let e,t,n=i[1]&&ce(i);return{c(){n&&n.c(),e=re()},m(o,s){n&&n.m(o,s),v(o,e,s),t=!0},p(o,[s]){o[1]?n?(n.p(o,s),s&2&&B(n,1)):(n=ce(o),n.c(),B(n,1),n.m(e.parentNode,e)):n&&(oe(),I(n,1,1,()=>{n=null}),se())},i(o){t||(B(n),t=!0)},o(o){I(n),t=!1},d(o){n&&n.d(o),o&&k(e)}}}function tt(i,e,t){let n,{component:o}=e,{component_props:s}=e,{value:r}=e;return i.$$set=l=>{"component"in l&&t(3,o=l.component),"component_props"in l&&t(0,s=l.component_props),"value"in l&&t(1,r=l.value)},i.$$.update=()=>{i.$$.dirty&8&&t(2,n=$e[o])},[s,r,n,o]}class lt extends M{constructor(e){super(),T(this,e,tt,et,j,{component:3,component_props:0,value:1})}}const ot=lt,st=["dynamic"];export{ot as Component,st as modes};
//# sourceMappingURL=index-edfa678c.js.map
