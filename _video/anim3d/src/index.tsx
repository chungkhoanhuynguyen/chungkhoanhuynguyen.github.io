import React from "react";
import { Composition, registerRoot } from "remotion";
import { PhoDemo, PHO_FRAMES } from "./videos/pho/Pho";
import { VangVideo, VANG_FRAMES } from "./videos/vang/Vang";
import { Bia } from "./videos/vang/Bia";
import { DatVideo, DAT_FRAMES } from "./videos/dat/Dat";
import { BiaDat } from "./videos/dat/BiaDat";
import { BiaHn } from "./videos/hn/BiaHn";
import { BiaLuong2 } from "./videos/luong2/BiaLuong2";
import { Ltc1Video, LTC1_FRAMES } from "./videos/ltc1/Ltc1";
import { LopQT } from "./videos/ltc1/LopQT";
import { HnVideo, HN_FRAMES } from "./videos/hn/Hn";
import { LuongVideo, LUONG_FRAMES } from "./videos/luong/Luong";
import { Luong2Video, LUONG2_FRAMES } from "./videos/luong2/Luong2";
const Root: React.FC = () => <>
  <Composition id="PhoDemo" component={PhoDemo} durationInFrames={PHO_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Vang" component={VangVideo} durationInFrames={VANG_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Dat" component={DatVideo} durationInFrames={DAT_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Hn" component={HnVideo} durationInFrames={HN_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Luong" component={LuongVideo} durationInFrames={LUONG_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="Luong2" component={Luong2Video} durationInFrames={LUONG2_FRAMES} fps={30} width={1920} height={1080} />

  <Composition id="Ltc1" component={Ltc1Video} durationInFrames={LTC1_FRAMES} fps={30} width={1920} height={1080} />
  <Composition id="LopQT" component={LopQT} durationInFrames={1} fps={30} width={1920} height={1080} />
  <Composition id="BiaLuong2" component={BiaLuong2} durationInFrames={1} fps={30} width={1920} height={1080} />
  <Composition id="BiaHn" component={BiaHn} durationInFrames={1} fps={30} width={1920} height={1080} />
  <Composition id="BiaDat" component={BiaDat} durationInFrames={1} fps={30} width={1920} height={1080} />
  <Composition id="Bia" component={Bia} durationInFrames={1} fps={30} width={1920} height={1080} />
</>;
registerRoot(Root);
