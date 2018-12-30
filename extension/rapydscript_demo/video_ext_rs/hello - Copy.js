var RS_modules = {};
RS_modules["math"] = {};

(function(){
    var __name__ = "math";
    var pi, e, isnan;
    pi = Math.PI;
    e = Math.E;
    function ceil(x) {
        return Math.ceil(x);
    }
    function copysign(x, y) {
        x = Math.abs(x);
        if (y < 0) {
            return -x;
        } else {
            return x;
        }
    }
    function fabs(x) {
        return Math.abs(x);
    }
    function factorial(x) {
        var RS_1;
        var r;
        if (((RS_1 = Math.abs(parseInt(x))) !== x && (typeof RS_1 !== "object" || !RS_eq(RS_1, x)))) {
            throw new ValueError("factorial() only accepts integral values");
        }
        factorial.cache = [];
        r = function(n) {
            if (n === 0 || n === 1) {
                return 1;
            }
            if (!factorial.cache[n]) {
                factorial.cache[n] = r(n - 1) * n;
            }
            return factorial.cache[n];
        };
        return r(x);
    }
    function floor(x) {
        return Math.floor(x);
    }
    function fmod(x, y) {
        while (y <= x) {
            x -= y;
        }
        return x;
    }
    function fsum(iterable) {
        var RSitr1, RSidx1, RSitr2, RSidx2, RSupk1;
        var partials, x, i, y, hi, lo;
        partials = [];
        RSitr1 = RS_Iterable(iterable);
        for (RSidx1 = 0; RSidx1 < RSitr1.length; RSidx1++) {
            x = RSitr1[RSidx1];
            i = 0;
            RSitr2 = RS_Iterable(partials);
            for (RSidx2 = 0; RSidx2 < RSitr2.length; RSidx2++) {
                y = RSitr2[RSidx2];
                if (Math.abs(x) < Math.abs(y)) {
                    RSupk1 = [ y, x ];
                    x = RSupk1[0];
                    y = RSupk1[1];
                }
                hi = x + y;
                lo = y - (hi - x);
                if (lo) {
                    partials[i] = lo;
                    ++i;
                }
                x = hi;
            }
            partials.splice(i, partials.length - i, x);
        }
        return sum(partials);
    }
    function isinf(x) {
        return !isFinite(x);
    }
    isnan = isNaN;
    function modf(x) {
        var m;
        m = fmod(x, 1);
        return [m, x - m];
    }
    function trunc(x) {
        return x | 0;
    }
    function exp(x) {
        return Math.exp(x);
    }
    function expm1(x) {
        if (Math.abs(x) < 1e-5) {
            return x + .5 * x * x;
        } else {
            return Math.exp(x) - 1;
        }
    }
    function log(x, base) {
        base = base === void 0 ? e : base;
        return Math.log(x) / Math.log(base);
    }
    function log1p(x) {
        var ret, n, i;
        ret = 0;
        n = 50;
        if (x <= -1) {
            return Number.NEGATIVE_INFINITY;
        }
        if (x < 0 || x > 1) {
            return Math.log(1 + x);
        }
        for (i = 1; i < n; i++) {
            if (i % 2 === 0) {
                ret -= Math.pow(x, i) / i;
            } else {
                ret += Math.pow(x, i) / i;
            }
        }
        return ret;
    }
    function log10(x) {
        return Math.log(x) / Math.LN10;
    }
    function pow(x, y) {
        var RS_2;
        if (x < 0 && ((RS_2 = parseInt(y)) !== y && (typeof RS_2 !== "object" || !RS_eq(RS_2, y)))) {
            throw new ValueError("math domain error");
        }
        if (isnan(y) && x === 1) {
            return 1;
        }
        return Math.pow(x, y);
    }
    function sqrt(x) {
        return Math.sqrt(x);
    }
    function acos(x) {
        return Math.acos(x);
    }
    function asin(x) {
        return Math.asin(x);
    }
    function atan(x) {
        return Math.atan(x);
    }
    function atan2(y, x) {
        return Math.atan2(y, x);
    }
    function cos(x) {
        return Math.cos(x);
    }
    function sin(x) {
        return Math.sin(x);
    }
    function hypot(x, y) {
        return Math.sqrt(x * x + y * y);
    }
    function tan(x) {
        return Math.tan(x);
    }
    function degrees(x) {
        return x * 180 / pi;
    }
    function radians(x) {
        return x * pi / 180;
    }
    function acosh(x) {
        return Math.log(x + Math.sqrt(x * x - 1));
    }
    function asinh(x) {
        return Math.log(x + Math.sqrt(x * x + 1));
    }
    function atanh(x) {
        return .5 * Math.log((1 + x) / (1 - x));
    }
    function cosh(x) {
        return (Math.exp(x) + Math.exp(-x)) / 2;
    }
    function sinh(x) {
        return (Math.exp(x) - Math.exp(-x)) / 2;
    }
    function tanh(x) {
        return (Math.exp(x) - Math.exp(-x)) / (Math.exp(x) + Math.exp(-x));
    }
    RS_modules["math"]["pi"] = pi;

    RS_modules["math"]["e"] = e;

    RS_modules["math"]["isnan"] = isnan;

    RS_modules["math"]["ceil"] = ceil;

    RS_modules["math"]["copysign"] = copysign;

    RS_modules["math"]["fabs"] = fabs;

    RS_modules["math"]["factorial"] = factorial;

    RS_modules["math"]["floor"] = floor;

    RS_modules["math"]["fmod"] = fmod;

    RS_modules["math"]["fsum"] = fsum;

    RS_modules["math"]["isinf"] = isinf;

    RS_modules["math"]["modf"] = modf;

    RS_modules["math"]["trunc"] = trunc;

    RS_modules["math"]["exp"] = exp;

    RS_modules["math"]["expm1"] = expm1;

    RS_modules["math"]["log"] = log;

    RS_modules["math"]["log1p"] = log1p;

    RS_modules["math"]["log10"] = log10;

    RS_modules["math"]["pow"] = pow;

    RS_modules["math"]["sqrt"] = sqrt;

    RS_modules["math"]["acos"] = acos;

    RS_modules["math"]["asin"] = asin;

    RS_modules["math"]["atan"] = atan;

    RS_modules["math"]["atan2"] = atan2;

    RS_modules["math"]["cos"] = cos;

    RS_modules["math"]["sin"] = sin;

    RS_modules["math"]["hypot"] = hypot;

    RS_modules["math"]["tan"] = tan;

    RS_modules["math"]["degrees"] = degrees;

    RS_modules["math"]["radians"] = radians;

    RS_modules["math"]["acosh"] = acosh;

    RS_modules["math"]["asinh"] = asinh;

    RS_modules["math"]["atanh"] = atanh;

    RS_modules["math"]["cosh"] = cosh;

    RS_modules["math"]["sinh"] = sinh;

    RS_modules["math"]["tanh"] = tanh;
})();

var __name__ = "__main__";
var factorial = RS_modules["math"].factorial;

function res() {
    var a;
    a = factorial(3);
    return a;
}
document.getElementById("s").innerHTML = res();