import matplotlib.pyplot as plt
from flask import Flask, render_template, request


app = Flask(__name__)


def function(fun, x):
    fun.replace('x', str(x))
    res = eval(fun)
    return res


@app.route("/", methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        return render_template('menu.html')
    else:
        a_a = 0
        b_b = 0
        h = request.form.get('h_h')
        try:
            if eval(h) or float(h):
                h = eval(h)
        except NameError:
            return render_template('Error_h.html')

        a = request.form.get('a_h')
        try:
            if eval(a) or float(a):
                a_a = eval(a)
        except NameError:
            return render_template('Error_a.html')

        b = request.form.get('b_h')
        try:
            if eval(b) or float(b):
                b_b = eval(b)
        except NameError:
            return render_template('Error_b.html')

        if a_a >= b_b:
            return render_template('Error_pred.html')
        else:
            plt.xlabel("x")
            plt.ylabel("y")
            # fig = plt.figure()

            xs = []
            ys = []

            func = request.form.get('func_h')
            n = (b_b - a_a) / h
            n = round(n)
            tmp = a_a
            first_step = function(func, a_a) + function(func, b_b)
            ax = plt.gca()

            xs.append(a_a)
            ys.append(function(func, a_a))
            # ax.axvline(a_a, 0, function(func, a_a), color='#ff0000')

            for k in range(1, n):
                # plt.fill(ys, tmp, 'b', alpha=0.2)
                tmp = tmp + h
                # ax.axvline(tmp, 0, function(func, tmp), color="#43a043")
                ax.axvline(tmp, color='#43a043')
                xs.append(tmp)
                first_step = first_step + 2 * function(func, tmp)
                print(function(func, tmp))
                ys.append(function(func, tmp))

            xs.append(b_b)
            ys.append(function(func, b_b))
            # plt.fill_between(xs, ys, np.zeros_like, ys, color='cyan')
            ax.axvline(a_a, color="#ff0000")
            ax.axvline(b_b, color="#ff0000")
            # ax.axvline(b_b, 0, function(func, b_b), color='#ff0000')
            # plt.fill_between(xs, ys, np.zeros_like, ys, color='cyan')
            plt.plot(xs, ys)
            # plt.show()
            plt.savefig('static/image.png')
            result = (h / 2) * first_step
            # fig = plt.subplots(figsize=(10, 10))
            plt.close()

            return render_template('result.html', res_val=result)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
