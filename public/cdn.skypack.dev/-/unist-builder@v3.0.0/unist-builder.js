var t = function(e, r, n) {
    var i = {
        type: String(e)
    };
    return n == null && (typeof r == "string" || Array.isArray(r)) ? n = r : Object.assign(i, r), Array.isArray(n) ? i.children = n : n != null && (i.value = String(n)), i
};
export {
    t as u
};
export default null;