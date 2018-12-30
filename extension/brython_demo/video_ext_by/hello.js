var ՐՏ_modules = {};
ՐՏ_modules["math"] = {};

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
        var ՐՏ_1;
        var r;
        if (((ՐՏ_1 = Math.abs(parseInt(x))) !== x && (typeof ՐՏ_1 !== "object" || !ՐՏ_eq(ՐՏ_1, x)))) {
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
        var ՐՏitr1, ՐՏidx1, ՐՏitr2, ՐՏidx2, ՐՏupk1;
        var partials, x, i, y, hi, lo;
        partials = [];
        ՐՏitr1 = ՐՏ_Iterable(iterable);
        for (ՐՏidx1 = 0; ՐՏidx1 < ՐՏitr1.length; ՐՏidx1++) {
            x = ՐՏitr1[ՐՏidx1];
            i = 0;
            ՐՏitr2 = ՐՏ_Iterable(partials);
            for (ՐՏidx2 = 0; ՐՏidx2 < ՐՏitr2.length; ՐՏidx2++) {
                y = ՐՏitr2[ՐՏidx2];
                if (Math.abs(x) < Math.abs(y)) {
                    ՐՏupk1 = [ y, x ];
                    x = ՐՏupk1[0];
                    y = ՐՏupk1[1];
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
        var ՐՏ_2;
        if (x < 0 && ((ՐՏ_2 = parseInt(y)) !== y && (typeof ՐՏ_2 !== "object" || !ՐՏ_eq(ՐՏ_2, y)))) {
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
    ՐՏ_modules["math"]["pi"] = pi;

    ՐՏ_modules["math"]["e"] = e;

    ՐՏ_modules["math"]["isnan"] = isnan;

    ՐՏ_modules["math"]["ceil"] = ceil;

    ՐՏ_modules["math"]["copysign"] = copysign;

    ՐՏ_modules["math"]["fabs"] = fabs;

    ՐՏ_modules["math"]["factorial"] = factorial;

    ՐՏ_modules["math"]["floor"] = floor;

    ՐՏ_modules["math"]["fmod"] = fmod;

    ՐՏ_modules["math"]["fsum"] = fsum;

    ՐՏ_modules["math"]["isinf"] = isinf;

    ՐՏ_modules["math"]["modf"] = modf;

    ՐՏ_modules["math"]["trunc"] = trunc;

    ՐՏ_modules["math"]["exp"] = exp;

    ՐՏ_modules["math"]["expm1"] = expm1;

    ՐՏ_modules["math"]["log"] = log;

    ՐՏ_modules["math"]["log1p"] = log1p;

    ՐՏ_modules["math"]["log10"] = log10;

    ՐՏ_modules["math"]["pow"] = pow;

    ՐՏ_modules["math"]["sqrt"] = sqrt;

    ՐՏ_modules["math"]["acos"] = acos;

    ՐՏ_modules["math"]["asin"] = asin;

    ՐՏ_modules["math"]["atan"] = atan;

    ՐՏ_modules["math"]["atan2"] = atan2;

    ՐՏ_modules["math"]["cos"] = cos;

    ՐՏ_modules["math"]["sin"] = sin;

    ՐՏ_modules["math"]["hypot"] = hypot;

    ՐՏ_modules["math"]["tan"] = tan;

    ՐՏ_modules["math"]["degrees"] = degrees;

    ՐՏ_modules["math"]["radians"] = radians;

    ՐՏ_modules["math"]["acosh"] = acosh;

    ՐՏ_modules["math"]["asinh"] = asinh;

    ՐՏ_modules["math"]["atanh"] = atanh;

    ՐՏ_modules["math"]["cosh"] = cosh;

    ՐՏ_modules["math"]["sinh"] = sinh;

    ՐՏ_modules["math"]["tanh"] = tanh;
})();

var __name__ = "__main__";
var math = ՐՏ_modules["math"];

function res() {
    var a;
    a = math.factorial(3);
    return a;
}
document.getElementById("s").innerHTML = res();