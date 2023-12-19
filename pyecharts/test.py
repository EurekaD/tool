import os
import random

from pyecharts.charts import Map
from pyecharts import options as opts


def values(rge, start: int = 20, end: int = 150) -> list:
    ar = [random.randint(start, end) for _ in range(rge)]
    print(ar)
    return ar


if __name__ == '__main__':

    hangzhou = ["滨江区", "淳安县", "富阳区", "拱墅区", "建德市", "临安区", "临平区", "钱塘区", "上城区", "桐庐县", "西湖区", "萧山区", "临平区", "余杭区"]

    print("正在导出{}地图...")

    html_path = "./html/map_hangzhou.html"
    if os.path.exists(html_path):
        os.remove(html_path)

    geojson_path = "./geojson/jingan.json"
    with open(geojson_path, "r", encoding="utf-8") as file:
        stream = file.read()

    Map().add_js_funcs("echarts.registerMap('杭州市',{});", stream) \
        .add("商家A", [list(z) for z in zip(hangzhou, values(len(hangzhou), 20, 150))], "杭州") \
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-{}地图".format("杭州")),
        visualmap_opts=opts.VisualMapOpts()
    ).render(html_path)

    print("{}地图导出完成，文件路径:{}".format("杭州", html_path))